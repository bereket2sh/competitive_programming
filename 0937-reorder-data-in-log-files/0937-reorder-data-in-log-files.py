class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log = []
        digit_log = []
        for log in logs:
            if log[-1].isalpha():
                letter_log.append(log)
            else:
                digit_log.append(log)

        letter_log.sort(key=lambda l: (l.split()[1:], l.split()[0]))
        return letter_log + digit_log