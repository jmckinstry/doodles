A collection of string reversal doodles.

---

perfect.py:
Given an array of characters comprised of alphanumerics and spaces, swap the order of the words while not changing the words themselves. Bonus points for in-place.

My first thought was to swap outer words and then work inwards, but that quickly showed the challenge: words have varying lengths. If you want to be in-place, where do the left-over or non-fitting characters go?

Second thought was to just reverse the whole string so we don't stomp anything.

That lends itself very quickly to the solution I came up with: Two reverses. Reverse the whole string, then reverse each word to put it back to rights.

It's O(3n), one n for the first reversal, one n looking for spaces, one n for the reversal of each word ommiting spaces.