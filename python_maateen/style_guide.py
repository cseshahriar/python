# কোড ইনডেন্ট করার সময় আমরা সব সময় চারটি স্পেস ব্যবহার করব। আর লাইন কন্টিনিউ (continue) করার 
# সময় প্রথম, দ্বিতীয় বা তৃতীয় বন্ধনীর ক্ষেত্রে এদের সাথে ভার্টিকালি (উল্লম্বভাবে) ইনডেন্ট করব।
foo = long_function_name(var_one, var_two,
                        var_three, var_four)

foo = long_function_name(var_one, var_two,
    var_three, var_four)

# hanging indemt
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

"""আমরা চাইলে ভার্টিকালি ইন্ডেন্ট না করে হ্যাংগিং (hanging) ইন্ডেন্টও ব্যবহার করতে পারি। এইক্ষেত্রে প্রথম 
লাইনে কোন আর্গুমেন্ট রাখব না আর পরের লাইন থেকে লাইন কন্টিনিউয়েশনের (continuation) 
মত করে ইন্ডেন্ট করব। """
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# ফাংশনের আর্গুমেন্ট বেশি হলে চারটার বদলে আটটা স্পেস দিয়ে শুধু আর্গুমেন্টগুলোকে ইন্ডেন্ট করলে ভাল হয়।
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# কন্ডিশনাল লজিকের কন্ডিশন বেশি লম্বা হলে লাইন কন্টিনিউয়েশন হিসাবে ইন্ডেন্ট করা যায়।
if (this_is_one_thing
        and that_is_another_thing):
    do_something()


# প্রথম, দ্বিতীয় ও তৃতীয় বন্ধনীর জোড়ের ক্ষেত্রে শেষ বন্ধনীটা কয়েকভাবে ইনডেন্ট করা যায়।
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )

# or
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

# ট্যাব নাকি স্পেস
# আমরা সবসময় স্পেস দিয়েই ইনডেন্ট করব। তবে কোন প্রোগ্রামে যদি ইতিমধ্যে ট্যাব ব্যবহার করা হয়ে থাকে,
#  সেখানে ট্যাব ব্যবহার করব আমরা। কারণ পাইথন-৩ এ স্পেস ও ট্যাবের মিশ্রণ দূষনীয়

""" 
লাইন লেন্থ
একটা লাইন সর্বোচ্চ ৭৯ ক্যারেক্টারের হতে পারবে। তবে ডকস্ট্রিং বা কমেন্টের মত বড়সড় টেক্সট ব্লকের ক্ষেত্রে প্রতিটা 
লাইন ৭২ ক্যারেক্টারের ভিতর সীমবদ্ধ থাকা উচিত। সীমার চেয়ে বড় হয়ে গেলে লাইন কন্টিনিউয়েশন ইন্ডেন্টেশন ব্যবহার করব। 
যেসব ক্ষেত্রে সাধারণ কন্টিনিউয়েশন ইন্ডেন্টেশন ব্যবহার করা যায় না সেখানে ব্যাকস্লাশ \ ব্যবহার করব।
"""
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())

""" 
বাইনারি অপারেটর আর লাইন ব্রেক
বহু বছর ধরে, বাইনারি অপারেটর ব্যবহারের ক্ষেত্রে লাইন ব্রেক অপারেটরের পরে হচ্ছে।
"""
# bad 
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

# কিন্তু তা রিড্যাবিলিটি নষ্ট করে বলে আমরা সবসময় বাইনারি অপারেটর ব্যবহারের ক্ষেত্রে লাইন ব্রেক অপারেটরের আগে ব্যবহার করব।
# good
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
          

"""
ব্লাঙ্ক লাইন - শূন্যে ভরা জীবন
টপ লেভেল ফাংশন ও ক্লাস ডেফিনিশনের আগে-পরে দুইটা ব্লাঙ্ক লাইন দিব আমরা।

ক্লাসের ভিতর মেথড ডেফিনিশনের আগে-পরে একটা ব্লাঙ্ক লাইন দিব আমরা।

ইমপোর্ট - আমদানি প্রকল্প
আমদানির ক্ষেত্রে সবসময় সেপারেট লাইন ব্যবহার করব আমরা। 
"""
# good
import os
import sys

# নিচের মত কখনোই করব না।
# bad 
import sys, os

"""
তবে from … import এর হিসাব আলাদা।

from subprocess import Popen, PIPE
মডিউল আমদানি সবসময় ফাইলের শুরুতে হবে। তবে একটা মডিউল আমদানির আগে সেই সম্পর্কিত কমেন্ট বা ডকস্ট্রিং থাকতে পারে। আর মডিউলগুলি বিভিন্ন গ্রুপে ভাগ করে আমদানি করব আমরা। প্রথমে আমদানি করব স্টান্ডার্ড মডিউল, তারপর করব থার্ড-পার্টি মডিউল এবং সবার শেষে লোকাল মডিউল। প্রতিটা গ্রুপকে ব্লাঙ্ক লাইন দিয়ে আলাদা করব আমরা। আর পারতপক্ষে ওয়াইল্ডকার্ড আমদানি (from <module> import *) করব না।

হাইলি রিড্যাবল বলে যথাসম্ভব অ্যাবসলিউট ইমপোর্ট ব্যবহার করব।
"""
# standart 
import mypkg.sibling
# third party
from mypkg import sibling
# local
from mypkg.sibling import example


# কমপ্লেক্স প্যাকেজের ক্ষেত্রে রিলেটিভ ইমপোর্ট ব্যবহার করা যায়।
from . import sibling
from .sibling import example


# কোন মডিউল থেকে কোন ক্লাসকে আমদানি করতে চাইলে এভাবে করব:

from myclass import MyClass
from foo.bar.yourclass import YourClass

# অবশ্য লোকাল ক্লাসের সাথে ক্লাশ হলে এভাবে আমদানি করব:
import myclass
import foo.bar.yourclass

""" 
মডিউল লেভেল ডান্ডার নেইম
মডিউল লেভেল ডান্ডার নেইম (যেমন: __all__, __author__, __version__) সবসময় মডিউল 
ডকস্ট্রিংয়ের পরে আর কোন মডিউল আমদানি করার আগে (from __future__ import ... ব্যতীত) ডিক্লেয়ার করব।
"""

"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys

# ওয়ান-লাইন ডকস্ট্রিং
# নাম শুনেই বোঝা যাচ্ছে, এসব ডকস্ট্রিং থাকবে মাত্র এক লাইন জুড়ে এবং সর্বোচ্চ ৭৯ ক্যারেক্টারের হবে লাইনটি। এর আগে-পিছে কোন ব্লাঙ্ক লাইন থাকবে না। তবে ক্লাসের ডকস্ট্রিংয়ের পর একটা ব্লাঙ্ক লাইন রাখা উচিত।

def kos_root():
    """Return the pathname of the KOS root directory."""
    global _kos_root
    if _kos_root: return _kos_root
    

# মাল্টি-লাইন ডকস্ট্রিং
# ডকস্ট্রিং কয়েকটা লাইনে লেখা হয়। সাধারণত ক্লাসের ক্ষেত্রে মাল্টি-লাইন ডকস্ট্রিং ব্যবহৃত হয়। প্রথমে ক্লাসের বর্ণনা আর তারপরে আর্গুমেন্টের বর্ণনা থাকে। আর্গুমেন্টের বর্ণনার ক্ষেত্রে প্রতিটি আর্গুমেন্টের জন্য পৃথক লাইন বরাদ্দ করা উচিত।

def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero


# হোয়াইটস্পেস
# প্রথম, দ্বিতীয় ও তৃতীয় বন্ধনীর সাথে স্পেস দেয়া যাবে না।

spam(ham[1], {eggs: 2})

# নিচের মত হবে না।
spam( ham[ 1 ], { eggs: 2 } )

# কমা, সেমিকোলন ও কোলনের আগে স্পেস দেয়া যাবে না।
if x == 4: print x, y; x, y = y, x

# নিচের মত হবে না।
if x == 4 : print x , y ; x , y = y , x


# বাইনারি অপারেটরের আগে-পরে স্পেস না দিলেও চলে। তবে দিলে সমান সংখ্যক স্পেস হবে। কোলন যখন বাইনারি 
# অপারেটর তখন কোলনের ক্ষেত্রেও এই নিয়ম প্রযোজ্য।

ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

# অ্যাসাইনমেন্ট অপারেটরের আগে পরে কেবল একটি করে স্পেস হবে।
x = 1
y = 2
long_variable = 3

# যদি কয়েকটি অপারেটরের মধ্যে গুরুত্ব কম-বেশি থাকে, তবে যেটার গুরুত্ব সবচেয়ে কম, এর আগে-পরে স্পেস দিতে হবে। যেমন -
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# ফাংশনের কীওয়ার্ড আর্গুমেন্ট বা ডিফল্ট প্যারামিটারের ক্ষেত্রে = চিহ্নের আগে-পরে কোন স্পেস হবে না।
def complex(real, imag=0.0):
    return magic(r=real, i=imag)


"""
নেমিং কনভেনশন
পাইথনে নেমিং কনভেনশন একটু জগাখিঁচুড়ি টাইপের, আমরা কখনোই সামঞ্জস্যপূর্ণ কিছু পাব না এখানে। তাই আমরা আপাতত স্টান্ডার্ড কিছু কনভেনশনে চোখ বুলাব।

b (একটামাত্র ছোট হাতের অক্ষর)

B (একটামাত্র বড় হাতের অক্ষর)

lowercase

lower_case_with_underscores

UPPERCASE

UPPER_CASE_WITH_UNDERSCORES

CapitalizedWords (অথবা CapWords বা CamelCase – উটের পিঠের মত বলে এরকম নামকরণ)। StudlyCaps নামেও পরিচিত।

নোট: CapWords এ অ্যাব্রিভিয়েশন ব্যবহার করার ক্ষেত্রে অ্যাব্রিভিয়েশনের সব কয়টা লেটারকে বড় হাতের অক্ষর করতে হবে। এইভাবে HTTPServerError, HttpServerError থেকে উত্তম নামকরণ।

mixedCase (শুরুতে ছোট হাতের অক্ষর কিন্তু পরে বড় হাতের অক্ষর)

Capitalized_Words_With_Underscores (বিশ্রী নামকরণ!)
"""

"""
সি++ বা জাভার মত পাইথনে পাবলিক, প্রাইভেট আইডিয়া নাই। পাইথনে সবকিছুই পাবলিক। তবে কনভেনশন দ্বারা 
এদের ব্যবহার আলাদা করা যায়। ক্লাস, মেথডের নামের আগে একটা আন্ডারস্কোর থাকলে তাকে প্রোটেক্টেড ধরা যায়। 
অপরপক্ষে ডাবল আন্ডারস্কোর থাকলে প্রাইভেট ধরা হয়। 
"""

""" 
পরিহারযোগ্য নাম
নামের ক্ষেত্রে কখনো l (এল), O (ও) এবং I (আই) ব্যবহার করা ঠিক না। বিভিন্ন ফন্টে এরা 
মিলেমিশে একাকার হয়ে যেতে পারে।
"""

"""
ক্লাস ও এক্সসেপশনের নাম
ক্লাসের নামের ক্ষেত্রে সাধারণত CapWords কনভেনশন মানা হয়। এক্সসেপশন যেহেতু ক্লাস তাই এর নামও CapWords
 কনভেনশন মেনে হবে। তবে নামের শেষে (নামের সাথেই) অবশ্যই Error কথাটা থাকতে হবে। 
"""

# প্রোগ্রামিং রিকমেন্ডেশন
# None এর মত সিঙ্গেলটনের সাথে কম্পেয়ার করার ক্ষেত্রে == অপারেটরের পরিবর্তে is অথবা is not ব্যবহার করা উচিত।
#  অন্যদিকে not ... is ব্যবহার করার চেয়ে is not অপারেটর ব্যবহার করাই উত্তম।
# global
if foo is not None:

# নিচের মত হবে না।
# bad
if not foo is None:

# ল্যাম্বডাকে কোন আইডেন্টিফায়ারে অ্যাসাইন করে কাজ সিদ্ধ না করে সব সময় def স্টেটমেন্ট ব্যবহার করা উচিত।
def f(x): return 2*x

# নিচের মত হবে না।
f = lambda x: 2*x

# ফাংশনের শেষে অবশ্যই একটা রিটার্ন স্টেটমেন্ট থাকা উচিত।

# লিস্ট, টাপল, ডিকশনারির এম্পটি কিনা সেটা চেক করার যায় নিচের মত করে:
if not seq:
if seq:

# নিচের মত হবে না।
if len(seq):
if not len(seq):

# বুলিয়ান ভ্যালুকে == অপারেটর ব্যবহার করে True বা False এর সাথে তুলনা করা উচিত না।
if greeting:

# নিচের মত হবে না।
if greeting == True:
if greeting is True: