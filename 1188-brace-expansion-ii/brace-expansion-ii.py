class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.s = expression
        self.i = 0

        result = self.parse_expression()

        return sorted(result)

    # expression = term (',' term)*
    def parse_expression(self):
        result = self.parse_term()

        while self.i < len(self.s) and self.s[self.i] == ',':
            self.i += 1

            next_term = self.parse_term()
            result |= next_term

        return result

    # term = factor+
    def parse_term(self):
        result = {""}

        while self.i < len(self.s):
            ch = self.s[self.i]

            # End of this expression
            if ch in "},":
                break

            factor = self.parse_factor()

            # Cartesian product / concatenation
            result = {
                a + b
                for a in result
                for b in factor
            }

        return result

    # factor = letter | '{' expression '}'
    def parse_factor(self):
        ch = self.s[self.i]

        # Single letter
        if ch.isalpha():
            self.i += 1
            return {ch}

        # Braced expression
        self.i += 1  # skip '{'

        result = self.parse_expression()

        self.i += 1  # skip '}'

        return result
        