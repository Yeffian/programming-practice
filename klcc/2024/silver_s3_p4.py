def solve(s):
    letters = dict()
    for c in s:
        if c in letters.keys():
            letters[c] += 1
        else:
            letters[c] = 1

    print(max(letters.values()) - min(letters.values()))

solve('NTRTRAJ87RQ9V9PBLGQ3DRN5IHXJMZU7LITS4EY34J1KX69AU29ZZZAPHAETWQ6XUS12QA4H3XDQ236K9LNR80HA0GPOHAQYT2B895SMPDGILUGCNZCQH26M9AZIAQVOL0TDCDCUBA580NIMKY1174NEC6Z1POXZNXUQ2Y3BMXCRO566HKJ7MR7NP55SXIEPR97TWQIL')
solve('xu8colbxnxug4uz0vskvfxbfcmjivct8qgysqasojdcddtkpcboploff3jssc1qx7hopypyvtekzwslhkvs9l1nxv6osq57smsdfuufkfipqamsudswzsedhv9fiaqd19uskwwmz0nn8guezhgqdrlzzrebphygfbq8gjrd3iaomzvnjhrbykhha5xjgsgouhlo7mh8gfnslila2dnwtavk4tzyuvpch1g9p1uevmfeg5bw8uswrux9fskbzbt0vclgfqadbroxocz3gnfpjk1g8h9mxuwe8pj51vquzlhsyeifzhnitjwk0slnbw9kzaoa5vfmscrythhk8lb9cqnzow21lidguvqeqsexgazigqctql8jbofvhyu7jcgckzdegpplqczwqkewclwero3qewijyyoj2cafahocb7ohzeomd4tw2xirefbwzbc4fumdmzt1bpiy3w3dzeuc7r8c2gdnolmxw0coq3vzq8dityuipywit')