# create a dictionary with the translations
# of each letter and number.

morse_letter = dict(
    ma = '.-',
    mb = '-...',
    mc = '-.-.',
    mch = '----',
    md = '-..',
    me = '.',
    mf = '..-.',
    mg = '--.',
    mh = '....',
    mi = '..',
    mj = '.---',
    mk = '-.-',
    ml = '.-..',
    mm = '--',
    mn = '-.',
    mñ = '--.--',
    mo = '---',
    mp = '.--.',
    mq = '--.-',
    mr = '.-.',
    ms = '...',
    mt = '-',
    mu = '..-',
    mv = '...-',
    mw = '.--',
    mx = '-..-',
    my = '-.--',
    mz = '--..',
    m0 = '-----',
    m1 = '.----',
    m2 = '..---',
    m3 = '...--',
    m4 = '....-',
    m5 = '.....',
    m6 = '-....',
    m7 = '--...',
    m8 = '---..',
    m9 = '----.',
    dot = '.-.-.-',
    slash = '-..-.',
    inter = '..--..',
    comma = '--..--',
    quot = '.-..-.'
    )

morse_to_letter = {
  ".-": "a",
  "-...": "b",
  "-.-.": "c",
  "----": "ch",
  "-..": "d",
  ".": "e",
  "..-.": "f",
  "--.": "g",
  "....": "h",
  "..": "i",
  ".---": "j",
  "-.-": "k",
  ".-..": "l",
  "-.": "n",
  "--": "m",
  "--.--": "ñ",
  "---": "o",
  ".--.": "p",
  "--.-": "q",
  ".-.": "r",
  "...": "s",
  "-": "t",
  "..-": "u",
  "...-": "v",
  ".--": "w",
  "-..-": "x",
  "-.--": "y",
  "--..": "z",
  "/": " ",
  ".----": "1",
  "..---": "2",
  "...--": "3",
  "....-": "4",
  ".....": "5",
  "-....": "6",
  "--...": "7",
  "---..": "8",
  "----.": "9",
  "-----": "0",
  ".-.-.-": "/",
  "-..-.": ".",
  "..--..": "?",
  "--..--": ",",
  ".-..-.": '"'
}