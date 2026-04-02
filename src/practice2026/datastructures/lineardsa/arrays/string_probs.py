# Encode and decode string leetcode - 659

from typing import List


class EncoderDecoder:

    # Steps for encode and decode
    # 1.Given a list of strings convert to string
    # 2.Add a length of each word in start of string word and the Delimiter e.g. 4#neet
    # 3. combine all strings in this way into one string

    # Encode the string
    def encode(self, strs: List[str]):
        # extract each word
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s  # e.g. strs = ["neet"] -> res = "4#neet"
        return res

    # Decode the string
    # Get the encoded string and separate the length 4 and delimiter # from each word
    def decode(self, str: str):
        # A list and counter i
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1  # Assume j is at #
            length = int(str[i:j])  # 0 -> j-1 is length no.
            i = j + 1
            j = i + length
            res.append(
                str[i:j]
            )  # assume -> j+1 at 1 index : 1 | length = 4 so => j+1 + length = 4
            i = j
        return res


if __name__ == "__main__":
    encDec = EncoderDecoder()
    strs = ["neet", "code"]
    encoded = encDec.encode(strs)
    print(encoded)
    print("Decoded is: ")
    print(encDec.decode(encoded))
