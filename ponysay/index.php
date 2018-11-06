<html>
<head>
	<title>Ponysay!</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
<body class="body_foreground body_background" style="font-size: normal;">
<link rel="stylesheet" type="text/css" href="ponysay.css">
<pre class="ansi2html-content">
<?php
putenv('LANG=en_US.UTF-8');

$path_to_pony_files = "/usr/share/ponysay/ponies";

$modes = array(
	"Pony",
	"Fortune",
	"Manual",
);
$ponies = explode("\n", shell_exec("ls -fA1 $path_to_pony_files/*.pony | sed -E -e ".escapeshellarg("s/^.*\\/(\w+)\\.pony$/\\1/g")));
array_unshift($ponies, ""); // Blank for random

$with_header = isset($_GET["with_header"]);
$thinking = isset($_GET["think"]);
$mode = isset($_GET["mode"]) ? $_GET["mode"] : "Pony";
$input = isset($_GET["input"]) ? $_GET["input"] : "";
$pony = isset($_GET["pony"]) ? $_GET["pony"] : "";
$result = "";


function print_header($modes, $ponies, $with_header, $mode, $input, $pony, $thinking) {
	print "<div name=\"header\">";
	print "<form name=\"input\">";

	print "<select name=\"mode\">";
	foreach ($modes as $key) {
		print "<option value=\"$key\"";
		if ($key === $mode) print" selected";
		print ">$key</option>";
	}
	print "</select>";
	print "<br />";

	print "<select name=\"pony\">";
	foreach ($ponies as $key) {
		print "<option value=\"$key\"";
		if ($key === $pony) print" selected";
		print ">$key</option>";
	}
	print "</select>";
	print "<br />";

	print "<textarea name=\"input\">".htmlspecialchars($input)."</textarea>";
	print "<br />";

	print "<input name=\"think\" type=\"checkbox\"".($thinking ? " checked" : "").">Thinking</input>";
	print "<br />";

	print "<input name=\"with_header\" type=\"checkbox\" checked>With Config</input>";
	print "<br />";

	print "<input name=\"submit\" type=\"submit\" action=\"/?with_header\" value=\"Generate\" />";
	print "</form>";

	print "<hr />";
}

function get_output($mode, $input, $pony, $thinking) {
	$output_filter = "ansi2html -i 2>/dev/null";
	$mode = strtolower($mode);
	$ponysay = ($thinking ? "ponythink" : "ponysay") . " -X -W i";

	if ($mode !== "pony" && !empty($pony)) $pony = "-F ".escapeshellarg($pony);

	if ($mode === "pony") {
		// Input follows a split standard here: -q is left blank or gives the pony directly, no -F required
		return shell_exec("$ponysay -q $pony | $output_filter");
	}
	else if ($mode === "fortune") {
		return shell_exec("fortune | $ponysay $pony | $output_filter");
	}
	else if ($mode === "manual") {
		// Have to filter inputs because we'll be sending them to a command line!
		$input = escapeshellarg($input);
		return shell_exec("$ponysay $pony $input | $output_filter");
	}
	else
		return "Invalid mode: $mode";
}

if ($with_header) print_header($modes, $ponies, $with_header, $mode, $input, $pony, $thinking);

$result = get_output($mode, $input, $pony, $thinking);
print $result;
?>
</pre>
</body>
</html>

