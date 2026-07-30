class Solution:
    def fullJustify(self, words, maxWidth):

        result = []                  # Final justified lines
        current_line = []            # Words in current line
        letters = 0                  # Total letters in current line

        for word in words:

            # Check if adding this word exceeds width
            if letters + len(word) + len(current_line) > maxWidth:

                spaces = maxWidth - letters

                # Only one word in line
                if len(current_line) == 1:

                    line = current_line[0] + " " * spaces

                else:

                    gaps = len(current_line) - 1

                    even = spaces // gaps

                    extra = spaces % gaps

                    line = ""

                    for i in range(gaps):

                        line += current_line[i]

                        line += " " * (even + (1 if i < extra else 0))

                    line += current_line[-1]

                result.append(line)

                current_line = []
                letters = 0

            current_line.append(word)
            letters += len(word)

        last = " ".join(current_line)

        last += " " * (maxWidth - len(last))

        result.append(last)

        return result