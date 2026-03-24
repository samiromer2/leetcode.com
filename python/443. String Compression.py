class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0   # where we write
        read = 0    # where we read

        while read < len(chars):
            char = chars[read]
            count = 0

            # count the group
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # write the character
            chars[write] = char
            write += 1

            # write count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write