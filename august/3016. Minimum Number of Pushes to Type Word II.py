class Solution:

    def minimumPushes(self, word: str) -> int:
        MAX_BUTTONS = 8
        count_keys = 0
        pushes = 0
        for key in Counter(word).most_common():
            pushes += key[1] * (1 + count_keys // MAX_BUTTONS)
            count_keys += 1
        return pushes
