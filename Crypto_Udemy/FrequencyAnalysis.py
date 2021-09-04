cipher = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""

class Attack:
  def _init_(self):
    self.alphabet = "abcdefghijklmnopqrstuvwxyz"
    self.freq = {}

  def calculate_freq(self, cipher):
    for c in self.alphabet:
      self.freq[c] = 0

      letter_count = 0
      for c in cipher:
        if c in self.freq:
          self.freq[c] += 1
          letter_count += 1

      for c in self.freq:
        self.freq[c] = round(self.freq[c]/letter_count, 4)

  def print_freq(self):
    for c in self.freq:
      print(c, ':', self.freq[c])
attack = Attack()
attack._init_()
attack.calculate_freq(cipher)
attack.print_freq()



# alphabet = "abcdefghijklmnopqrstuvwxyz"

# freq = {}
# for c in alphabet:
#     freq[c] = 0

# letter_count = 0
# for c in cipher:
#     if c in freq:
#         freq[c] += 1
#         letter_count += 1

# for c in freq:
#     freq[c] = round(freq[c]/letter_count, 4)
# new_line_count = 0

# for c in freq:
#     print(c, ':', freq[c])
    
        
