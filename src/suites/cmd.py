# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cmd.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: juligonz <juligonz@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/07/15 15:11:46 by charles           #+#    #+#              #
#    Updated: 2020/09/16 16:57:42 by juligonz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import distutils

import config
from suite import suite


@suite()
def suite_redirection(test):
    test("echo bonjour > test", setup="", files=["test"])
    test("echo > test bonjour", setup="", files=["test"])
    test("> test echo bonjour", setup="", files=["test"])
    test("echo bonjour >> test", setup="", files=["test"])
    test("echo >> test bonjour", setup="", files=["test"])
    test(">> test echo bonjour", setup="", files=["test"])
    test("cat < test", setup="echo bonjour > test")
    test("echo bonjour > test", setup="", files=["test"])

    test("echo > test'sticked' bonjour", setup="", files=["teststicked"])
    test("> test'sticked' echo bonjour", setup="", files=["teststicked"])
    test("echo bonjour >> test'sticked'", setup="", files=["teststicked"])
    test("echo >> test'sticked' bonjour", setup="", files=["teststicked"])
    test(">> test'sticked' echo bonjour", setup="", files=["teststicked"])
    test("cat < test'sticked'", setup="echo bonjour > test'sticked'")
    test("< test'sticked' cat", setup="echo bonjour > test'sticked'")

    test("echo > test\"sticked\" bonjour", setup="", files=["teststicked"])
    test("> test\"sticked\" echo bonjour", setup="", files=["teststicked"])
    test("echo bonjour >> test\"sticked\"", setup="", files=["teststicked"])
    test("echo >> test\"sticked\" bonjour", setup="", files=["teststicked"])
    test(">> test\"sticked\" echo bonjour", setup="", files=["teststicked"])
    test("cat < test\"sticked\"", setup="echo bonjour > test\"sticked\"")
    test("< test\"sticked\" cat", setup="echo bonjour > test\"sticked\"")

    test("echo > test'yo'\"sticked\" bonjour", setup="", files=["testyosticked"])
    test("> test'yo'\"sticked\" echo bonjour", setup="", files=["testyosticked"])
    test("echo bonjour >> test'yo'\"sticked\"", setup="", files=["testyosticked"])
    test("echo >> test'yo'\"sticked\" bonjour", setup="", files=["testyosticked"])
    test(">> test'yo'\"sticked\" echo bonjour", setup="", files=["testyosticked"])
    test("cat < test'yo'\"sticked\"", setup="echo bonjour > test'yo'\"sticked\"")
    test("< test'yo'\"sticked\" cat", setup="echo bonjour > test'yo'\"sticked\"")

    test("echo bonjour > test > je > suis", setup="", files=["test", "je", "suis"])
    test("echo > test > je bonjour > suis", setup="", files=["test", "je", "suis"])
    test("> test echo bonjour > je > suis", setup="", files=["test", "je", "suis"])
    test("echo bonjour >> test > je >> suis", setup="", files=["test", "je", "suis"])
    test("echo >> test bonjour > je > suis", setup="", files=["test", "je", "suis"])
    test(">> test echo > je bonjour > suis", setup="", files=["test", "je", "suis"])
    test("cat < test < je", setup="echo bonjour > test; echo salut > je")

    test("echo bonjour>test>je>suis", setup="", files=["test", "je", "suis"])
    test(">test echo bonjour>je>suis", setup="", files=["test", "je", "suis"])
    test("echo bonjour>>test>je>>suis", setup="", files=["test", "je", "suis"])
    test("cat<test<je", setup="echo bonjour > test; echo salut > je")

    test("echo bonjour > a'b'c'd'e'f'g'h'i'j'k'l'm'n'o'p'q'r's't'u'v'w'x'y'z'",
            files=["abcdefghijklmnopqrstuvwxyz"])
    test('echo bonjour > a"b"c"d"e"f"g"h"i"j"k"l"m"n"o"p"q"r"s"t"u"v"w"x"y"z"',
            files=["abcdefghijklmnopqrstuvwxyz"])
    test('echo bonjour > a\'b\'c"d"e\'f\'g"h"i\'j\'k"l"m\'n\'o"p\'q\'r"s\'t\'u"v"w"x"y\'z\'',
            files=["abcdefghijklmnopqrstuvwxyz"])

    test("> file", files=["file"])
    test("< file", setup="echo bonjour > file")

    test(">")
    test(">>")
    test("<")
    test("echo >")
    test("echo >>")
    test("echo <")

    test("> test", files=["test"])
    test(">> test", files=["test"])
    test("< test", setup="touch test")

    test("echo foo >>> bar")
    test("echo foo >>>> bar")
    test("echo foo >>>>> bar")

    test("cat << < bar", setup="echo bonjour > bar")
    test("cat <<<< bar", setup="echo bonjour > bar")
    test("cat <<<<< bar", setup="echo bonjour > bar")

    test("cat < doesnotexist")


@suite()
def suite_cmd(test):
    test("notfound")
    test("notfound a b c")
    test('echo "\\"" >>a"b""c"  ', files=["abc"])
    test("echo foo>bar", files=["bar"])
    test("echo foo >bar", files=["bar"])
    test("echo foo> bar", files=["bar"])
    test("echo foo > bar", files=["bar"])


@suite()
def suite_status(test):
    test("echo $?")
    test("echo; echo $?")
    test("notfound; echo $?")
    test("cat < doesntexist; echo $?")
    test("cat < noperm; echo $?", setup="echo bonjour > noperm; chmod 000 noperm")

    test("echo")
    test("notfound")
    test("cat < doesntexist")
    test("cat < noperm", setup="echo bonjour > noperm; chmod 000 noperm")


@suite()
def suite_cmd_path(test):
    ls_path = distutils.spawn.find_executable("ls")
    cat_path = distutils.spawn.find_executable("cat")

    test(ls_path, setup="touch a b c")
    test(ls_path + " -l", setup="touch a b c")
    test("./bonjour", setup="touch a b c; cp {} bonjour".format(ls_path))
    test("./bonjour -l", setup="touch a b c; cp {} bonjour".format(ls_path))
    test("./somedir/bonjour -l",
            setup="mkdir somedir; touch a b c; touch somedir/d somedir/e;" +
                  "cp {} somedir/bonjour".format(ls_path))

    test("./ls . a b c",
            setup="touch a b c; echo bonjour > a; cp {} ls".format(cat_path))
    test("ls . a b c",
            setup="touch a b c; echo bonjour > a; cp {} ls".format(cat_path))

    test("./somefile", setup="touch somefile; chmod 000 somefile")
    test("./somefile", setup="touch somefile; chmod 001 somefile")
    test("./somefile", setup="touch somefile; chmod 002 somefile")
    test("./somefile", setup="touch somefile; chmod 003 somefile")
    test("./somefile", setup="touch somefile; chmod 004 somefile")
    test("./somefile", setup="touch somefile; chmod 005 somefile")
    test("./somefile", setup="touch somefile; chmod 006 somefile")
    test("./somefile", setup="touch somefile; chmod 007 somefile")
    test("./somefile", setup="touch somefile; chmod 010 somefile")
    test("./somefile", setup="touch somefile; chmod 020 somefile")
    test("./somefile", setup="touch somefile; chmod 030 somefile")
    test("./somefile", setup="touch somefile; chmod 040 somefile")
    test("./somefile", setup="touch somefile; chmod 050 somefile")
    test("./somefile", setup="touch somefile; chmod 060 somefile")
    test("./somefile", setup="touch somefile; chmod 070 somefile")
    test("./somefile", setup="touch somefile; chmod 100 somefile")
    test("./somefile", setup="touch somefile; chmod 200 somefile")
    test("./somefile", setup="touch somefile; chmod 300 somefile")
    test("./somefile", setup="touch somefile; chmod 400 somefile")
    test("./somefile", setup="touch somefile; chmod 500 somefile")
    test("./somefile", setup="touch somefile; chmod 600 somefile")
    test("./somefile", setup="touch somefile; chmod 700 somefile")

    test("./somefile", setup="touch somefile; chmod 755 somefile")
    test("./somefile", setup="touch somefile; chmod 644 somefile")
    test("./somefile", setup="touch somefile; chmod 311 somefile")
    test("./somefile", setup="touch somefile; chmod 111 somefile")
    test("./somefile", setup="touch somefile; chmod 222 somefile")
    test("./somefile", setup="touch somefile; chmod 333 somefile")

    test("somedir/",   setup="mkdir somedir")
    test("./somedir/", setup="mkdir somedir")
    test("somedir",    setup="mkdir somedir")
    test("./somedir",  setup="mkdir somedir")
    test("somedir",    setup="mkdir somedir")

    test("somedirsoftlink/",   setup="mkdir somedir; ln -s somedir somedirsoftlink")
    test("./somedirsoftlink/", setup="mkdir somedir; ln -s somedir somedirsoftlink")
    test("somedirsoftlink",    setup="mkdir somedir; ln -s somedir somedirsoftlink")
    test("./somedirsoftlink",  setup="mkdir somedir; ln -s somedir somedirsoftlink")
    test("somedirsoftlink",    setup="mkdir somedir; ln -s somedir somedirsoftlink")

    test("./someremovedlink",  setup="touch somefile; ln -s somefile someremovedlink; rm -f somefile")

    test("./somelink2", setup="touch somefile; ln -s somefile somelink1; ln -s somelink1 somelink2")
    test("./somelink3", setup="touch somefile; ln -s somefile somelink1; ln -s somelink1 somelink2;" +
                                               "ln -s somelink2 somelink3")
    test("./somelink4", setup="touch somefile; ln -s somefile somelink1; ln -s somelink1 somelink2;" +
                                               "ln -s somelink2 somelink3; ln -s somelink3 somelink4")

    test("./somelink2ls", setup="cp " + ls_path + " somefile;" +
                                "ln -s somefile somelink1; ln -s somelink1 somelink2")
    test("./somelink3ls", setup="cp " + ls_path + " somefile;" +
                                "ln -s somefile somelink1; ln -s somelink1 somelink2;" +
                                "ln -s somelink2 somelink3")
    test("./somelink4ls", setup="cp " + ls_path + " somefile;" +
                                "ln -s somefile somelink1; ln -s somelink1 somelink2;" +
                                "ln -s somelink2 somelink3; ln -s somelink3 somelink4")

    test("_", setup="touch _")
    test("'-'", setup="touch -")
    test("./_", setup="touch _")
    test("./-", setup="touch -")
    test("./.", setup="touch .")
    test("./..", setup="touch ..")

    test("./somefile", setup='touch somefile && chmod 0777 somefile')
    test("./somefile", setup='touch somefile && chmod 1000 somefile')
    test("./somefile", setup='touch somefile && chmod 2000 somefile')
    test("./somefile", setup='touch somefile && chmod 3000 somefile')
    test("./somefile", setup='touch somefile && chmod 4000 somefile')
    test("./somefile", setup='touch somefile && chmod 5000 somefile')
    test("./somefile", setup='touch somefile && chmod 6000 somefile')
    test("./somefile", setup='touch somefile && chmod 7000 somefile')
    test("./somefile", setup='touch somefile && chmod 1777 somefile')
    test("./somefile", setup='touch somefile && chmod 2777 somefile')
    test("./somefile", setup='touch somefile && chmod 3777 somefile')
    test("./somefile", setup='touch somefile && chmod 4777 somefile')
    test("./somefile", setup='touch somefile && chmod 5777 somefile')
    test("./somefile", setup='touch somefile && chmod 6777 somefile')
    test("./somefile", setup='touch somefile && chmod 7777 somefile')
    test("./somefile", setup='touch somefile && chmod 0000 somefile')

    test("./somedir", setup='mkdir somedir && chmod 0777 somedir')
    test("./somedir", setup='mkdir somedir && chmod 1000 somedir')
    test("./somedir", setup='mkdir somedir && chmod 2000 somedir')
    test("./somedir", setup='mkdir somedir && chmod 3000 somedir')
    test("./somedir", setup='mkdir somedir && chmod 4000 somedir')
    test("./somedir", setup='mkdir somedir && chmod 5000 somedir')
    test("./somedir", setup='mkdir somedir && chmod 6000 somedir')
    test("./somedir", setup='mkdir somedir && chmod 7000 somedir')
    test("./somedir", setup='mkdir somedir && chmod 1777 somedir')
    test("./somedir", setup='mkdir somedir && chmod 2777 somedir')
    test("./somedir", setup='mkdir somedir && chmod 3777 somedir')
    test("./somedir", setup='mkdir somedir && chmod 4777 somedir')
    test("./somedir", setup='mkdir somedir && chmod 5777 somedir')
    test("./somedir", setup='mkdir somedir && chmod 6777 somedir')
    test("./somedir", setup='mkdir somedir && chmod 0000 somedir')

# @suite(bonus=True)
# def suite_cmd_variable(test):
#     test("A=a sh -c 'echo $A'")
#     test("A=a B=b sh -c 'echo $A$B'")
#     test("A=a B=b C=c D=d E=e F=f G=g H=h sh -c 'echo $A$B$C$D$E$F$G$H'")
#     test("A=a A=bonjour sh -c 'echo $A'")
#     test("A=aA=bonjour sh -c 'echo $A'")
#     test("BONJOURJESUIS=a sh -c 'echo $BONJOURJESUIS'")
#     test("bonjourjesuis=a sh -c 'echo $bonjourjesuis'")
#     test("bonjour_je_suis=a sh -c 'echo $bonjour_je_suis'")
#     test("BONJOURJESUIS1=a sh -c 'echo $BONJOURJESUIS1'")
#     test("bO_nJq123o__1ju_je3234sui__a=a sh -c 'echo $bO_nJq123o__1ju_je3234sui__a'")
#     test("a0123456789=a sh -c 'echo $a0123456789'")
#     test("abcdefghijklmnopqrstuvwxyz=a sh -c 'echo $abcdefghijklmnopqrstuvwxyz'")
#     test("ABCDEFGHIJKLMNOPQRSTUVWXYZ=a sh -c 'echo $ABCDEFGHIJKLMNOPQRSTUVWXYZ'")
#     test("__________________________=a sh -c 'echo $__________________________'")
#     test("_bonjour_=a sh -c 'echo $_bonjour_'")
#     test("_=a sh -c 'echo $_a'")
#     test("1=a")
#     test("BONJOURJESUIS =a sh -c 'echo $BONJOURJESUIS '")
#     test("BONJOURJESUIS= a sh -c 'echo $BONJOURJESUIS'")
#     test(r"BONJOUR\\JESUIS=a sh -c 'echo $BONJOUR\\JESUIS'")
#     test(r'BONJOUR\'JESUIS=a sh -c "echo $BONJOUR\'JESUIS"')
#     test(r'BONJOUR\"JESUIS=a sh -c "echo $BONJOUR\"JESUIS"')
#     test(r"BONJOUR\$JESUIS=a sh -c 'echo $BONJOUR\$JESUIS'")
#     test(r"BONJOUR\&JESUIS=a sh -c 'echo $BONJOUR\&JESUIS'")
#     test(r"BONJOUR\|JESUIS=a sh -c 'echo $BONJOUR\|JESUIS'")
#     test(r"BONJOUR\;JESUIS=a sh -c 'echo $BONJOUR\;JESUIS'")
#     test(r"BONJOUR\_JESUIS=a sh -c 'echo $BONJOUR\_JESUIS'")
#     test(r"BONJOUR\0JESUIS=a sh -c 'echo $BONJOUR\0JESUIS'")
#     test(r"\B\O\N\ \ \ \ \ \ \ JOURJESUIS=a sh -c 'echo $\B\O\N\ \ \ \ \ \ \ JOURJESUIS'")
#     test(r"A=\B\O\N\ \ \ \ \ \ \ JOURJESUIS sh -c 'echo $A'")
#     test(r"A='bonjour je suis charles' sh -c 'echo $A'")
#     test(r'A="bonjour je suis charles" sh -c "echo $A"')
#     test(r"A==a sh -c 'echo $A'")
#     test(r"A===a sh -c 'echo $A'")
#     test(r"A====a sh -c 'echo $A'")
#     test(r"A=====a sh -c 'echo $A'")
#     test(r"A======a sh -c 'echo $A'")
#     test(r"A=a=a=a=a=a sh -c 'echo $A'")
#
#     test("A=a; echo $A")
#     test("A=a B=b; echo $A$B")
#     test("A=a B=b C=c D=d E=e F=f G=g H=h; echo $A$B$C$D$E$F$G$H")
#     test("A=a A=bonjour; echo $A")
#     test("A=aA=bonjour; echo $A")
#     test("BONJOURJESUIS=a; echo $BONJOURJESUIS")
#     test("bonjourjesuis=a; echo $bonjourjesuis")
#     test("bonjour_je_suis=a; echo $bonjour_je_suis")
#     test("BONJOURJESUIS1=a; echo $BONJOURJESUIS1")
#     test("bO_nJq123o__1ju_je3234sui__a=a; echo $bO_nJq123o__1ju_je3234sui__a")
#     test("a0123456789=a; echo $a0123456789")
#     test("abcdefghijklmnopqrstuvwxyz=a; echo $abcdefghijklmnopqrstuvwxyz")
#     test("ABCDEFGHIJKLMNOPQRSTUVWXYZ=a; echo $ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#     test("__________________________=a; echo $__________________________")
#     test("_bonjour_=a; echo $_bonjour_")
#     test("_=a; echo $_a")
#     test("BONJOURJESUIS =a; echo $BONJOURJESUIS ")
#     test("BONJOURJESUIS= a; echo $BONJOURJESUIS")
#     test(r"BONJOUR\\JESUIS=a; echo $BONJOUR\\JESUIS")
#     test(r"BONJOUR\'JESUIS=a; echo $BONJOUR\'JESUIS")
#     test(r'BONJOUR\"JESUIS=a; echo $BONJOUR\"JESUIS')
#     test(r"BONJOUR\$JESUIS=a; echo $BONJOUR\$JESUIS")
#     test(r"BONJOUR\&JESUIS=a; echo $BONJOUR\&JESUIS")
#     test(r"BONJOUR\|JESUIS=a; echo $BONJOUR\|JESUIS")
#     test(r"BONJOUR\;JESUIS=a; echo $BONJOUR\;JESUIS")
#     test(r"BONJOUR\_JESUIS=a; echo $BONJOUR\_JESUIS")
#     test(r"BONJOUR\0JESUIS=a; echo $BONJOUR\0JESUIS")
#     test(r"\B\O\N\ \ \ \ \ \ \ JOURJESUIS=a; echo $\B\O\N\ \ \ \ \ \ \ JOURJESUIS")
#     test(r"A=\B\O\N\ \ \ \ \ \ \ JOURJESUIS; echo $A")
#     test(r"A='bonjour je suis charles'; echo $A")
#     test(r'A="bonjour je suis charles"; echo $A')
#     test(r"A==a; echo $A")
#     test(r"A===a; echo $A")
#     test(r"A====a; echo $A")
#     test(r"A=====a; echo $A")
#     test(r"A======a; echo $A")
#     test(r"A=a=a=a=a=a; echo $A")
#
#     test("PATH=a ls")
#     test("PATH=a echo aa")
#     test("A=a echo $A")
#     test("A=a B=b echo $A$B")
#     test("A=a B=b C=c D=d E=e F=f G=g H=h echo $A$B$C$D$E$F$G$H")
#     test("A=$PATH sh -c 'echo $A'")
#     test("A=\"$PATH je  suis\" sh -c 'echo $A'")
#     test("A='$PATH je  suis' sh -c 'echo $A'")
#     test("$TEST sh -c 'echo $A'", setup="export TEST='A=a'")
#     test("'BONJOURJESUIS''=''a' sh -c 'echo $BONJOURJESUIS'")
#     test('"BONJOURJESUIS""=""a" sh -c "echo $BONJOURJESUIS"')
#     test("./somedir", setup='mkdir somedir && chmod 0000 somedir')
