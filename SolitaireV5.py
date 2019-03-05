#!/usr/local/bin/python3

# ---------
# Python implementation of Bruce Schneier's Solitaire Encryption
# Algorithm (http://www.counterpane.com/solitaire.html).
#
# Based on original code by John Dell'Aquila <jbd@alum.mit.edu>
#
# Updated for python 3
#
# Added functionality to output a keyed deck. The idea is to speed
# up the manual process if your keying multiple decks or some such
# thing. Did the same for shuffling and added a bridge ordered deck
# output for those that don't remember the order. Found a great
# write up at https://aarontoponce.org/wiki/crypto/card-ciphers/solitaire
# to help with understanding, he did a youtube as well that makes
# it easy to digest.
#
# -- r0gu3b17 (r0gu3b17@gmail.com)
# -----BEGIN PGP PUBLIC KEY BLOCK-----
# 
# xsFNBFx6lUIBEACd2rjZvywHb4PraYcrMs6vnHfgtuFtyg927djT8ybNwc2mRhG9wSWzOR7p2IaW
# 8kgeqDkC0oaNqgBDKzMK7EDs4nzRgYRIMtx4TfzcNYBDp+vg4bo8UyWOA64JTW5lqCfMG3B3N9Jj
# wkz+xCSN4jFX4oYMsYsj52Y2VNI9qHT7wUq7aXW+T+nfmOHYUdpaNej1360ZX/+xmaNLB/pgSgDG
# 9JSFBlY6SS4GKQLqC8jb9WSwABaVZl4Xmk2sLz3xanxcDU9cjOoH2SigLbKFXcloNwYHgoYroW1p
# 45ZrPccyN6cU+IhA8Ax1upg2XX8I/cCwsUppJqQQtT/1eRFRTc4Jl7pgLiTz+SRx8HfQs1ANwzzj
# 6C2z1c3NWUlEGT5vb/0ZIcZxkHBghlxkQAu7L59F3zNyebXaKDuK9zBhWYcD/PgapT/kV3TezTOP
# fPeXk8RZ/ahSg+Em1yAeM5Veb/0q2z4FrhS7RoR1FPspO4PO9G46hP0WHGTRJ2DF9CNzBWvTGg7m
# zFdk0tAygt55rFMfyV4C6EipeNcveQJTxXI2KG4v1f3lRV6jBRG0AdNb3gEok9fe67bUPycLHWgy
# 0MfIANN4rD4GkFxYY6Ahz7r8+iOiZuJ09/aZpueclMmmTnkc+HjQ1vRuwq5dPpqmHKcvvQFC6SXi
# RGfQKSAKzVaWUwARAQABzR1yMGd1M2IxNyA8cjBndTNiMTdAZ21haWwuY29tPsLBcAQTAQoAGgUC
# XHqVQgIbAQMLCQcDFQoIAh4BAheAAhkBAAoJEMveM0sxgkW0Ab8P/ROgpenU/O2f0bL4h7wkTOX3
# YPxqiqG/R8eCXzk4JNcSkYB+JyVLmsLwbYCoS6g/E8Mr3+YezLeKQkEAO35yOVMk1x2bXD5VUIXI
# 4qeBPLcdd8iyLhOEfZ1MlQ1xWqV1Vcf8/DcFpOE+agE73qpm1uom93Fi0TIOSJzSc3umvaIjfJ9Q
# hR2ZnLEdg+ApF7ZZykPjPRVbt2HT1R5hvrK6m+Da5ioZcmShRGR+zdA9NGs/jHsl2Y4nZqbmI2aR
# Vv50/kYR6VhwX4pqj6PRsLun9EFNwyZf09EpAUPcHUek0khdXVrAXebu5YghyIka0nAKpYZPJvtO
# a6seQdrrYL88FIXOOKrUSV7FoYrKEX2l+j6ndrrGfq/mp1a1t+5hqNZJ1QFjUGJXI8CEiQD1NLXY
# 5yHhXIvBIy/FJGmk5ug3qyyGBpcii6d9/gQbmQ7kKdOgXfsWQBHLKdrO0eyr1T4q1AdDUXGMpCU7
# v73ad78PONWgNExbIAoEU+JoisQZToG5vyKNiCgpGrOH+rj+LurFxNgxgk4CtOWF51KX2WI81Bl7
# 9+aYVCMr5+7RMwKaM6QsrInPwcNvLb5BwfhopBkrcRHZP2qOriDdeXObolQxz+SWDReW5Xj8wOcx
# mif81GbnQeKaOsRF719qpNgyBI+3rAvwTERit0lwpvkq1pR3bODGzsBNBFx6lUIBCADQuDfR2hXw
# 3DefmkarNZRk3ppjag+my6v+vp7yRaZYko7ll0t/D86qcIjWx9rXgCc+y4R/h37fr2lZIP3x24Fp
# uJ58BNsuV3pW361vZJvAFUXmaCCcR8D1d7gYgBpI+naQ2uc/AKQMHz/radLMyD/riwfIUHbQT5Pf
# JRHaPqPtBn+ijtgVC5nCmppOemfgO5WoaDQlsVIY0lKCUteGkqYfdiUmtkbxVwvMgfRxjRoF8vfT
# 7a9F13jd0j54Oav98FQlb2IKK92KxK6rpCohSCTUupua7kCDjTwjTc6+ji07qBS3qd+EnY/eV82m
# IdNxffmkN9kwwh5Ofhm1QC7iU/HHABEBAAHCwoQEGAEKAA8FAlx6lUIFCQ8JnAACGwQBKQkQy94z
# SzGCRbTAXSAEGQEKAAYFAlx6lUIACgkQr7gbYRxRr/6Msgf/Wbxv3R8GCV9S7fOKJ4Ce2porJa2M
# u56/NnTme0EJAPL6R/3KAoNGKjaYy7c4F3aaa9zpEo6mGE39RYjiOCy8t0txIDUb+ATtpX3zl2sE
# JmneV4/dnfPw69HRBpzp/KSbicJCf/mqyAuqIt8XAezGnXg9pU9skyL6tx0KXcSKuQI2S/OBK0Ed
# 9hKD72iiU111mQ3h8cY3UproHQyP5s9RdSzNLW1Hm7LekZHRzYgYQ9+ObYb0eu/1wCu08UNRjqyH
# xtYGB7vQ+wQu4mn+O42iuv/WKQd12wqbyy3dnF0ZUYp9fZGjD7Yjr03wRxDJZ35QfTd2pD3mr00v
# EYgDBYDRcsRsD/9gTylc1NPuRfe+DjCberZrRZgP17GJa92KoqInNtB8KfNR5U6JCbtMHspT1oq5
# d1fgqviPr6XFqLx9mo5sK+kYcbNTdhcXfNigPm3KT6qJ8wiJ15WOR8HCdPcDeWAQfoGJaVmswIyr
# V+nQHo8E6OhwfMTesPJl73JNyk1fOMuwpbLIFVEOZ7GjaV56uyJcvBualtsqYu+qx6bwijxyDR18
# WigMaG+Eb1v5qF7Sfi1BFsjOLn9qMSgnB6qdiLjv53XXxZ4r2dhS3926icTsYsopYX3DN5s8kI8+
# +wkIYhjEGPDSwxg6od9naQYN1DGSZz0V/1LR0TJk7t9qvNqo5MVhjV21YbLqpLVoVGr5h0tBSjD3
# WAkqxgF2kucuP/s9RuRkKx/7FZy8m6JuBIGueT88jo4hN94I+gRtkMVX2fSJeclrd/eUsYjPp8cU
# imnHLAAAapJkOwCVP1f5dgnesVS5bQ2d9+CRiTjjnvC7YnDY170ow8QwfV3eHw7rtUvTSWtqdv4l
# 6oDGTrY22Q0pRKbuVqvANY07hYGqGsJ9ZqhcXiZuDJ47cLa0QqDoDPOLAUROpGOmxUZFG3DJhAne
# NbGV/4LhAAoa36LCYm6+p4FH/Bipwa9CWxd7EOqrQcuQEvBaCjLhlSqDyl8yDwj4x4LRpuPALppS
# gqUP/HQyLIxcbs7ATQRcepVCAQgAuFryQ3bHe+9BJ7E/m16I2Y1nGBZWd+O4GrTzc+BXK9xiiCYu
# JLo3W0ebWSGDrJEOLftaxcc+FCTJsUhiROpgRLUO3yc83FC024rMOrG6yn4rVb3p0NdldvVMhTx0
# qfkGV8xVK4txTR5uWewIfSfYidY+AMLzxZ8fBFu17ZsOwM0G6kNFoZZRnoER+ZhsAmVldvtvzHhc
# Sy+F6KT/GX8XMozRslnO6lVb6PXm5OZn4YudE4nGTJurps/D7HLHLTH96yvIU659KWF/lgGDF0m1
# FyP35+Yn24+RckwrvwHWm8nfde2UusSYrbg1i1vX2rWtoQ3/V47LdKiKEXw3YPwLtwARAQABwsKE
# BBgBCgAPBQJcepVCBQkPCZwAAhsiASkJEMveM0sxgkW0wF0gBBkBCgAGBQJcepVCAAoJEBFY4HSY
# No4dcLgIAIvj8ItDbWg4+zhVNPiey2edrEyxKzggvupLpAsMeG65gvuFxc0ASk0cWChGUshmAsTb
# 23qCChCHMFX0WWE7avNfBnayVFwnAp8kOmohrMkBWv6kefo1xx7B/OnBaOENQnGoLyeeyVJ9x2qH
# YxQs7u7EsJ4fbxj1+j60OypM7iYxlCKNINKoTXPSH3WMrKnz+GC3nkWd4bBeJY1dYcn3aROD43ED
# 6UE1dB54lgdYQJnknDn7ZK9SGNQEZEO71qYJsVO+WUljvWzEa2Bup3SUP/WqhF4ZUJ7IxIxcCh4E
# 7ipPePCS2kTgejoEIYzawDNlmKPcmVkBZ5vr/jX6LSgWPTDqDBAAnGr7IJHyWkyKtBiSravtkecy
# b+NRV4InaEecKXwh216UNOb2JyBi/wA4GgLC4+HBf5FXML2SHkQchLmfM1+rEJ0vCHUUCBhnuTSG
# JK+a/+BL+uOTmnPpKBfQkuqatUatG1N6MkXhvgQa6lS9o3YzDm1Nc0T1WfV7rh3bmH6p7kndUSe6
# 2tH9xyoipPUSWNjrStW5jcREZ8zjY5eS4AKIVF2qStbHejeqyjfw1Zlmjwcwb6WDRSTJjibPqJte
# HTToHYoW/PDJFUKDaL6CZoOoAp4yrRkQq6mDhp2pvmwqlFabYKXbCsFfhPOlfvdTWo17cEX0BFiG
# LI0mDIRwKkcKoKGGGhf1NUdRAhitpKD9YQswUKhc94d4+vbvaFkOM1TxaeiAerL6cAXBfuIQlChz
# dlVG7LU+jUPP2HrUbyi3Hq4vWbI2Dwgcup71vabf/aUx3uMmVC75r6J1MYkHGnm4cYtkQGr6GfZo
# qjigqr2wnyRpCErlD3XLyjExCwt2VBJ5oAyVCADr8Ku+Jom3yKWF28BERowmdcwiXQUgqTHcECGU
# R1gFGm7l91X4Pa3DJKHO8l4UIIH6rstkWBFBUw77iFA4MSr/jrao35Gw+BRIQ9l4XPnNjuYEm3Os
# kbfdCcY46tu4E1NzbIBZeuE3R/nxM2KLGgr9/IzbNnsOjT1xk48=
# =dRQa
# -----END PGP PUBLIC KEY BLOCK-----
# ---------

import string, sys, argparse, random

def toNumber(c):
    # ---------
    # Convert letter to number: Aa->1, Bb->2, ..., Zz->26.
    # Non-letters are treated as X's.
    # ---------
    if c in string.ascii_letters:
        NumVal = ord(c.upper()) - 64
        return NumVal
    return 24  # 'X'

def toChar(n):
    # ---------
    # Convert number to letter: 1->A,  2->B, ..., 26->Z,
    # 27->A, 28->B, ... ad infitum
    # ---------
    return chr((n-1)%26+65)


class Solitaire:
    # --------- Solitaire Encryption Algorithm
    # http://www.counterpane.com/solitaire.html
    # ---------

    def _setKey(self, passphrase):
        # ---------
        # Order deck according to passphrase.
        # ---------
        self.deck = list(range(1,55))
        # card numbering:
        #  1, 2,...,13 are A,2,...,K of clubs
        # 14,15,...,26 are A,2,...,K of diamonds
        # 27,28,...,39 are A,2,...,K of hearts
        # 40,41,...,52 are A,2,...,K of spades
        # 53 & 54 are the A & B jokers
        for c in passphrase:
            self._round()
            self._countCut(toNumber(c))

    def _down1(self, card):
        # ---------
        # Move designated card down 1 position, treating
        # deck as circular.
        # ---------
        d = self.deck
        n = d.index(card)
        if n < 53: # not last card - swap with successor
            d[n], d[n+1] = d[n+1], d[n]
        else: # last card - move below first card
            d[1:] = d[-1:] + d[1:-1]

    def _tripleCut(self):
        # ---------
        # Swap cards above first joker with cards below
        # second joker.
        # ---------
        d = self.deck
        a, b = d.index(53), d.index(54)
        if a > b:
            a, b = b, a
        d[:] = d[b+1:] + d[a:b+1] + d[:a]

    def _countCut(self, n):
        # ---------
        # Cut after the n-th card, leaving the bottom
        # card in place.
        # ---------
        d = self.deck
        n = min(n, 53) # either joker is 53
        d[:-1] = d[n:-1] + d[:n]

    def _round(self):
        # ---------
        # Perform one round of keystream generation.
        # ---------
        self._down1(53) # move A joker down 1
        self._down1(54) # move B joker down 2
        self._down1(54)
        self._tripleCut()
        self._countCut(self.deck[-1])

    def _output(self):
        # ---------
        # Return next output card.
        # ---------
        d = self.deck
        while 1:
            self._round()
            topCard = min(d[0], 53)  # either joker is 53
            if d[topCard] < 53:  # don't return a joker
                return d[topCard]

    def encrypt(self, txt, key):
        # ---------
        # Return 'txt' encrypted using 'key'.
        # ---------
        self._setKey(key)
        txt = txt + 'X' * ((5-len(txt))%5)
        cipher = [None] * len(txt)
        for n in range(len(txt)):
            cipher[n] = toChar(toNumber(txt[n]) + self._output())
        for n in range(len(cipher)-5, 4, -5):
            cipher[n:n] = [' ']
        EncVal = ''.join(cipher)
        return EncVal

    def decrypt(self, cipher, key):
        # ---------
        # Return 'cipher' decrypted using 'key'.
        # ---------
        self._setKey(key)
        cipher = ''.join(cipher.split())
        txt = [None] * len(cipher)
        for n in range(len(cipher)):
            txt[n] = toChar(toNumber(cipher[n]) - self._output())
        DecVal = ''.join(txt)
        return DecVal

    def keydeck(self, key):
        # ---------
        # Return keyed deck
        # ---------
        self._setKey(key)
        return self.deck

    def shuffledeck(self):
        # ---------
        # Return keyed deck
        # ---------
        self.deck = list(range(1,55))
        random.shuffle(self.deck)
        return self.deck

    def bridgedeck(self):
        # ---------
        # Return keyed deck
        # ---------
        self.deck = list(range(1,55))
        return self.deck

    def cardValue(self, cardIdx):
        bridgeDeck = ['Ace of clubs',
                      '2 of clubs',
                      '3 of clubs',
                      '4 of clubs',
                      '5 of clubs',
                      '6 of clubs',
                      '7 of clubs',
                      '8 of clubs',
                      '9 of clubs',
                      '10 of clubs',
                      'jack of clubs',
                      'queen of clubs',
                      'king of clubs',
                      'Ace of diamonds',
                      '2 of diamonds',
                      '3 of diamonds',
                      '4 of diamonds',
                      '5 of diamonds',
                      '6 of diamonds',
                      '7 of diamonds',
                      '8 of diamonds',
                      '9 of diamonds',
                      '10 of diamonds',
                      'jack of diamonds',
                      'queen of diamonds',
                      'king of diamonds',
                      'Ace of hearts',
                      '2 of hearts',
                      '3 of hearts',
                      '4 of hearts',
                      '5 of hearts',
                      '6 of hearts',
                      '7 of hearts',
                      '8 of hearts',
                      '9 of hearts',
                      '10 of hearts',
                      'jack of hearts',
                      'queen of hearts',
                      'king of hearts',
                      'Ace of spades',
                      '2 of spades',
                      '3 of spades',
                      '4 of spades',
                      '5 of spades',
                      '6 of spades',
                      '7 of spades',
                      '8 of spades',
                      '9 of spades',
                      '10 of spades',
                      'jack of spades',
                      'queen of spades',
                      'king of spades',
                      'joker A',
                      'joker B']
        cardStr = bridgeDeck[cardIdx - 1]
        return cardStr

testCases = ( # test vectors from Schneier paper
    ('AAAAAAAAAAAAAAA', '', 'EXKYI ZSGEH UNTIQ'),
    ('AAAAAAAAAAAAAAA', 'f', 'XYIUQ BMHKK JBEGY'),
    ('AAAAAAAAAAAAAAA', 'fo', 'TUJYM BERLG XNDIW'),
    ('AAAAAAAAAAAAAAA', 'foo', 'ITHZU JIWGR FARMW'),
    ('AAAAAAAAAAAAAAA', 'a', 'XODAL GSCUL IQNSC'),
    ('AAAAAAAAAAAAAAA', 'aa', 'OHGWM XXCAI MCIQP'),
    ('AAAAAAAAAAAAAAA', 'aaa', 'DCSQY HBQZN GDRUT'),
    ('AAAAAAAAAAAAAAA', 'b', 'XQEEM OITLZ VDSQS'),
    ('AAAAAAAAAAAAAAA', 'bc', 'QNGRK QIHCL GWSCE'),
    ('AAAAAAAAAAAAAAA', 'bcd', 'FMUBY BMAXH NQXCJ'),
    ('AAAAAAAAAAAAAAAAAAAAAAAAA', 'cryptonomicon',
     'SUGSR SXSWQ RMXOH IPBFP XARYQ'),
    ('SOLITAIRE','cryptonomicon','KIRAK SFJAN')
)

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(description = 'An implementation of the Solitaire encryption algorithm, as designed by Bruce Schneier and described at: http://www.counterpane.com/solitaire.html')
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('--test', action='store_true', help='run test of implementation')
    group.add_argument('--bridgedeck', action='store_true', help='Bridge order a deck')
    group.add_argument('--shuffledeck', action='store_true', help='shuffle a deck')
    group.add_argument('--keydeck', help='key a deck')
    group.add_argument('--encrypt', help='encrypt a message')
    group.add_argument('--decrypt', help='decrypt a message')
    args = parser.parse_args()
    if args.test:
        s = Solitaire()
        for txt, key, cipher in testCases:
            coded = s.encrypt(txt, key)
            assert cipher == coded
            decoded = s.decrypt(coded, key)
            assert decoded[:len(txt)] == txt.upper()
        print('All tests passed\n')
    elif args.encrypt:
        if args.infile:
            print(Solitaire().encrypt(args.infile.read(), args.encrypt))
        else:
            print(Solitaire().encrypt(sys.stdin.read(), args.encrypt))
    elif args.decrypt:
        if args.infile:
            print(Solitaire().decrypt(args.infile.read(), args.decrypt))
        else:
            print(Solitaire().decrypt(sys.stdin.read(), args.decrypt))
    elif args.keydeck:
        d = Solitaire().keydeck(args.keydeck)
        print("Keyed deck:")
        for i in d:
            print("{}".format(Solitaire().cardValue(i)))
    elif args.shuffledeck:
        d = Solitaire().shuffledeck()
        print("Shuffled deck:")
        for i in d:
            print("{}".format(Solitaire().cardValue(i)))
    elif args.bridgedeck:
        d = Solitaire().bridgedeck()
        print("Bridge ordered deck:")
        for i in d:
            print("{}".format(Solitaire().cardValue(i)))
    else:
        parser.print_help()
