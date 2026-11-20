"""
Complete Synthesis of Class 10 Mathematics Chapter 14: Probability
Curriculum ID: 019778b1-dc6c-4660-9538-1940ec6cad64
100% NCERT Question & Example Coverage:
- Examples: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
- Exercise 14.1: Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25
All solved in Authentic Board Topper Layout: Given -> To Find/Prove -> Formula -> Step-by-Step -> [ROUGH_WORK] -> Boxed Answer.
Includes Page References, Section References, concise 2-5 word image_search_queries, and High-Precision Vector SVGs.
"""

import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "maths_class10_generators"))
from svg_builder_class10 import build_probability_svg

def get_ch14_complete_modules():
    CURRICULUM_ID = "019778b1-dc6c-4660-9538-1940ec6cad64"

    svg_dice = build_probability_svg(
        variant="dice_grid",
        title="Two-Dice Sample Space Grid (36 Outcomes)",
        caption="Sample Space S = {(1,1), (1,2), ..., (6,6)} | Diagonal sums highlight equal probability bands"
    )

    svg_cards = build_probability_svg(
        variant="cards_deck",
        title="52 Playing Cards Architectural Classification",
        caption="4 Suits (Spades ♠, Hearts ♥, Diamonds ♦, Clubs ♣) × 13 Cards | 12 Face Cards (J, Q, K)"
    )

    svg_coins = build_probability_svg(
        variant="coin_tree",
        title="Three-Coin Toss Binary Decision Tree",
        caption="2³ = 8 equally likely outcomes: HHH, HHT, HTH, HTT, THH, THT, TTH, TTT"
    )

    m1_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 199] Example 1: Find the probability of getting a head when a coin is tossed once. Also find the probability of getting a tail.",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 199,
            "image_search_query": "coin toss probability head tail",
            "has_diagram": True,
            "diagram_svg": svg_coins,
            "given": "A fair coin tossed once. Sample space S = {H, T}.",
            "formula": "Classical Probability: P(E) = (Number of outcomes favourable to E) / (Total number of possible outcomes).",
            "substitution": "Total possible outcomes n(S) = 2. Favourable to Head = {H} ⇒ 1. Favourable to Tail = {T} ⇒ 1.",
            "calculation": "P(Head) = 1/2 = 0.5. P(Tail) = 1/2 = 0.5. Sum of probabilities = 1/2 + 1/2 = 1.",
            "finalAnswer": "P(Head) = 1/2, P(Tail) = 1/2",
            "unit": "probability",
            "solution": "GIVEN:\nA fair unbiased coin is tossed once.\nSample space S = {H, T}.\nTotal number of elementary outcomes, n(S) = 2.\n\nTO FIND:\n(i) Probability of getting a Head, P(H).\n(ii) Probability of getting a Tail, P(T).\n\nFORMULA USED:\nP(E) = (Number of outcomes favourable to E) / (Total number of possible outcomes).\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Probability of getting a Head:\nFavourable outcome: {H} (1 outcome).\nP(H) = 1 / 2.\n\nStep 2: Probability of getting a Tail:\nFavourable outcome: {T} (1 outcome).\nP(T) = 1 / 2.\n\nNotice that P(H) + P(T) = 1/2 + 1/2 = 1, verifying that the sum of probabilities of all elementary events of an experiment is 1.\n\n[ROUGH_WORK]\n2 outcomes. Each equally likely: 1/2 = 0.5.\nBoxed Answer: [ P(Head) = 1/2, P(Tail) = 1/2 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 200] Example 2: A bag contains a red ball, a blue ball and a yellow ball, all the balls being of the same size. Kritika takes out a ball from the bag without looking into it. What is the probability that she takes out the (i) yellow ball? (ii) red ball? (iii) blue ball?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 200,
            "image_search_query": "colored balls probability bag random draw",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Bag contains 1 red ball, 1 blue ball, and 1 yellow ball. Total balls = 3.",
            "formula": "P(E) = n(E) / n(S).",
            "substitution": "Total outcomes n(S) = 3. Each color has 1 ball.",
            "calculation": "P(Yellow) = 1/3, P(Red) = 1/3, P(Blue) = 1/3.",
            "finalAnswer": "P(Yellow) = 1/3, P(Red) = 1/3, P(Blue) = 1/3",
            "unit": "probability",
            "solution": "GIVEN:\nA bag contains 1 red (R), 1 blue (B), and 1 yellow (Y) ball of identical size.\nTotal balls in bag, n(S) = 1 + 1 + 1 = 3.\n\nTO FIND:\n(i) P(Yellow), (ii) P(Red), (iii) P(Blue).\n\nFORMULA USED:\nP(E) = n(E) / n(S).\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Probability of Yellow ball:\nNumber of yellow balls = 1.\nP(Yellow) = 1 / 3.\n\nStep 2: Probability of Red ball:\nNumber of red balls = 1.\nP(Red) = 1 / 3.\n\nStep 3: Probability of Blue ball:\nNumber of blue balls = 1.\nP(Blue) = 1 / 3.\n\nNote: P(Y) + P(R) + P(B) = 1/3 + 1/3 + 1/3 = 1.\n\n[ROUGH_WORK]\n3 equally likely outcomes. 1/3 for each.\nBoxed Answer: [ (i) 1/3, (ii) 1/3, (iii) 1/3 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 200] Example 3: Suppose we throw a die once. (i) What is the probability of getting a number greater than 4? (ii) What is the probability of getting a number less than or equal to 4?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 200,
            "image_search_query": "die roll probability greater less than 4",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "A single fair 6-sided die thrown. Sample space S = {1, 2, 3, 4, 5, 6}. Total outcomes n(S) = 6.",
            "formula": "P(E) = n(E) / n(S).",
            "substitution": "(i) Greater than 4: {5, 6} ⇒ 2 outcomes. P = 2/6 = 1/3.\n(ii) Less than or equal to 4: {1, 2, 3, 4} ⇒ 4 outcomes. P = 4/6 = 2/3.",
            "calculation": "(i) 2/6 = 1/3. (ii) 4/6 = 2/3. Also P(E') = 1 - 1/3 = 2/3.",
            "finalAnswer": "(i) 1/3, (ii) 2/3",
            "unit": "probability",
            "solution": "GIVEN:\nA fair die is thrown once.\nSample space S = {1, 2, 3, 4, 5, 6}.\nTotal possible outcomes, n(S) = 6.\n\nTO FIND:\n(i) Probability of getting a number strictly greater than 4.\n(ii) Probability of getting a number less than or equal to 4.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Number greater than 4:\nFavourable outcomes = {5, 6}.\nNumber of favourable outcomes = 2.\nP(Number > 4) = 2 / 6 = 1 / 3.\n\nPart (ii): Number less than or equal to 4:\nFavourable outcomes = {1, 2, 3, 4}.\nNumber of favourable outcomes = 4.\nP(Number ≤ 4) = 4 / 6 = 2 / 3.\n\nNotice that 'Number ≤ 4' is the complementary event of 'Number > 4':\nP(Number ≤ 4) = 1 - P(Number > 4) = 1 - 1/3 = 2/3.\n\n[ROUGH_WORK]\n2/6 = 1/3. 4/6 = 2/3. Sum = 1.\nBoxed Answer: [ (i) 1/3, (ii) 2/3 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 201] Example 4: One card is drawn from a well-shuffled deck of 52 cards. Calculate the probability that the card will (i) be an ace, (ii) not be an ace.",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 201,
            "image_search_query": "deck 52 playing cards ace probability",
            "has_diagram": True,
            "diagram_svg": svg_cards,
            "given": "Deck of 52 cards. Total cards n(S) = 52. Number of aces = 4 (one in each suit).",
            "formula": "P(Ace) = n(Ace) / n(S). P(not Ace) = 1 - P(Ace).",
            "substitution": "(i) P(Ace) = 4 / 52 = 1 / 13.\n(ii) P(not Ace) = 1 - 1/13 = 12 / 13 (or 48 / 52 = 12 / 13).",
            "calculation": "(i) 4/52 = 1/13. (ii) 48/52 = 12/13.",
            "finalAnswer": "(i) 1/13, (ii) 12/13",
            "unit": "probability",
            "solution": "GIVEN:\nA well-shuffled standard deck of 52 playing cards.\nTotal possible outcomes, n(S) = 52.\n\nTO FIND:\n(i) Probability that the card is an Ace.\n(ii) Probability that the card is not an Ace.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Card is an Ace:\nA standard deck contains 4 aces (Ace of Spades, Hearts, Diamonds, Clubs).\nNumber of favourable outcomes = 4.\nP(Ace) = 4 / 52 = 1 / 13.\n\nPart (ii): Card is not an Ace:\nThe event 'not an ace' is the complement of the event 'an ace':\nP(not Ace) = 1 - P(Ace)\nP(not Ace) = 1 - 1/13 = 12 / 13.\n(Alternatively: Number of non-ace cards = 52 - 4 = 48. P = 48/52 = 12/13).\n\n[ROUGH_WORK]\n4/52 = 1/13. 1 - 1/13 = 12/13.\nBoxed Answer: [ (i) 1/13, (ii) 12/13 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 206] Exercise 14.1 Q1: Complete the following statements:\n(i) Probability of an event E + Probability of the event 'not E' = _______.\n(ii) The probability of an event that cannot happen is _______. Such an event is called _______.\n(iii) The probability of an event that is certain to happen is _______. Such an event is called _______.\n(iv) The sum of the probabilities of all the elementary events of an experiment is _______.\n(v) The probability of an event is greater than or equal to _______ and less than or equal to _______.",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 206,
            "image_search_query": "axiomatic probability rules impossible certain event",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Five fundamental theoretical principles of probability.",
            "formula": "Axioms of probability: P(E) + P(not E) = 1; P(impossible) = 0; P(sure) = 1; Σ P(ei) = 1; 0 ≤ P(E) ≤ 1.",
            "substitution": "(i) 1; (ii) 0, impossible event; (iii) 1, sure or certain event; (iv) 1; (v) 0, 1.",
            "calculation": "All statements completed per standard axiomatic probability definitions.",
            "finalAnswer": "(i) 1, (ii) 0; impossible event, (iii) 1; sure/certain event, (iv) 1, (v) 0; 1",
            "unit": "axioms",
            "solution": "GIVEN:\nFive theoretical statements defining the foundational axioms of classical probability.\n\nTO COMPLETE:\nFill each blank with the exact mathematical term or value.\n\nSTEP-BY-STEP CALCULATION / PROOF:\n(i) By the law of complementary events: P(E) + P(Ē) = 1.\n(ii) The probability of an event that cannot happen is 0. Such an event is called an IMPOSSIBLE EVENT.\n(iii) The probability of an event that is certain to happen is 1. Such an event is called a SURE or CERTAIN EVENT.\n(iv) The sum of the probabilities of all the elementary events of an experiment is 1.\n(v) The probability of an event is greater than or equal to 0 and less than or equal to 1 (0 ≤ P(E) ≤ 1).\n\n[ROUGH_WORK]\nKey axioms: P(E) + P(not E) = 1; range is [0, 1]; impossible = 0; sure = 1; sum of all elementary events = 1.\nBoxed Answer: [ (i) 1, (ii) 0, impossible event, (iii) 1, sure event, (iv) 1, (v) 0, 1 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 206] Exercise 14.1 Q2: Which of the following experiments have equally likely outcomes? Explain.\n(i) A driver attempts to start a car. The car starts or does not start.\n(ii) A player attempts to shoot a basketball. She/he shoots or misses the shot.\n(iii) A trial is made to answer a true-false question. The answer is right or wrong.\n(iv) A baby is born. It is a boy or a girl.",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 206,
            "image_search_query": "equally likely outcomes experiments explanation probability",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Four real-world experiments.",
            "formula": "Outcomes are equally likely if each outcome has the exact same chance of occurring based on intrinsic physical symmetry without bias.",
            "substitution": "(i) Not equally likely (depends on mechanical condition of car).\n(ii) Not equally likely (depends on skill of player).\n(iii) Equally likely (only 2 options: True or False).\n(iv) Equally likely (assuming natural birth probability of boy/girl is 1/2).",
            "calculation": "Experiments (iii) and (iv) have equally likely outcomes. (i) and (ii) do not.",
            "finalAnswer": "(iii) and (iv) have equally likely outcomes; (i) and (ii) do not",
            "unit": "conceptual reasoning",
            "solution": "GIVEN:\nFour experimental scenarios.\n\nTO DETERMINE:\nWhich experiments produce equally likely outcomes, with justification.\n\nSTEP-BY-STEP ANALYSIS:\n(i) Starting a car: NOT equally likely. Under normal working conditions, a car almost always starts. If defective, it may not start. The outcomes depend on mechanical factors and are not equally probable.\n(ii) Shooting a basketball: NOT equally likely. The likelihood of scoring depends on the player's skill, training, distance, and defense. Success and failure are not symmetrically equal.\n(iii) Answering a True/False question: EQUALLY LIKELY. In a purely randomized trial without bias, there are only two possibilities (True or False), each having an equal 50% probability (1/2).\n(iv) Baby born being a boy or a girl: EQUALLY LIKELY. Biologically and theoretically, the birth of a male or female child is mutually symmetric with equal probability of 1/2.\n\n[ROUGH_WORK]\nEqually likely means p = 0.5 each naturally. Only (iii) and (iv) satisfy this.\nBoxed Answer: [ (iii) and (iv) are equally likely; (i) and (ii) are not ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 206] Exercise 14.1 Q3: Why is tossing a coin considered to be a fair way of deciding which team should get the ball at the beginning of a football game?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 206,
            "image_search_query": "fair coin toss decision football game symmetry",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Tossing a fair coin to decide team possession.",
            "formula": "Symmetric probability: P(Head) = P(Tail) = 1/2. Outcomes are mutually exclusive and equally likely.",
            "substitution": "Neither team has any intrinsic advantage; the outcome is completely unpredictable and unbiased.",
            "calculation": "P(Head) = P(Tail) = 1/2 ⇒ Fair decision.",
            "finalAnswer": "Because the two outcomes (Head and Tail) are mutually exclusive and equally likely (probability 1/2 each), ensuring zero bias",
            "unit": "conceptual reasoning",
            "solution": "GIVEN:\nA standard coin toss at the beginning of a sports match.\n\nTO EXPLAIN:\nWhy tossing a coin is considered a fair method of making the decision.\n\nSTEP-BY-STEP REASONING / PROOF:\n1. A coin has two mutually exclusive faces: Head and Tail.\n2. When tossed, the coin rotates in a chaotic physical regime such that neither face is favored.\n3. The two outcomes are EQUALLY LIKELY, each having a probability of exactly 1/2:\n   P(Head) = P(Tail) = 1/2 = 0.5.\n4. The result is completely unbiased, independent, and unpredictable beforehand.\n5. Therefore, tossing a coin is a fair, impartial method for deciding possession.\n\n[ROUGH_WORK]\nP(Head) = P(Tail) = 0.5. Symmetric and unbiased.\nBoxed Answer: [ Outcomes are equally likely (probability 1/2 each) and unpredictable ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 206] Exercise 14.1 Q4: Which of the following cannot be the probability of an event?\n(A) 2/3  (B) -1.5  (C) 15%  (D) 0.7",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 206,
            "image_search_query": "probability range axiom non negative bounded 1",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Four numerical values: (A) 2/3 ≈ 0.67, (B) -1.5, (C) 15% = 0.15, (D) 0.7.",
            "formula": "Axiom of Probability: For any event E, 0 ≤ P(E) ≤ 1.",
            "substitution": "2/3 ∈ [0, 1]; 15% = 0.15 ∈ [0, 1]; 0.7 ∈ [0, 1]. -1.5 < 0 (negative, outside range).",
            "calculation": "Option (B) is negative, hence cannot be a probability.",
            "finalAnswer": "-1.5 (Option B)",
            "unit": "probability range",
            "solution": "GIVEN:\nFour numerical values: (A) 2/3, (B) -1.5, (C) 15%, (D) 0.7.\n\nTO FIND:\nWhich value cannot represent the probability of an event.\n\nFORMULA USED:\nBy the foundational axioms of probability, the probability P(E) of any event E must satisfy:\n0 ≤ P(E) ≤ 1.\nA probability can NEVER be negative, and can NEVER exceed 1.\n\nSTEP-BY-STEP CALCULATION:\n- (A) 2/3 = 0.666... lies in [0, 1] (Valid)\n- (B) -1.5 is negative (-1.5 < 0), which violates the non-negativity axiom (Invalid)\n- (C) 15% = 15/100 = 0.15 lies in [0, 1] (Valid)\n- (D) 0.7 lies in [0, 1] (Valid)\n\nTherefore, option (B) cannot be the probability of an event.\n\n[ROUGH_WORK]\nProbability cannot be negative. -1.5 < 0.\nBoxed Answer: [ -1.5 (Option B) ].",
            "concept_questions": []
        }
    ]

    m2_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 202] Example 5: Two players, Sangeeta and Reshma, play a tennis match. It is known that the probability of Sangeeta winning the match is 0.62. What is the probability of Reshma winning the match?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 202,
            "image_search_query": "tennis match complementary events probability",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "P(Sangeeta wins) = 0.62. Tennis matches cannot end in a draw, so Reshma winning is the complementary event of Sangeeta winning.",
            "formula": "P(Reshma wins) = 1 - P(Sangeeta wins).",
            "substitution": "P(Reshma wins) = 1 - 0.62 = 0.38.",
            "calculation": "1.00 - 0.62 = 0.38.",
            "finalAnswer": "0.38",
            "unit": "probability",
            "solution": "GIVEN:\nProbability of Sangeeta winning, P(S) = 0.62.\n\nTO FIND:\nProbability of Reshma winning, P(R).\n\nFORMULA USED:\nSince a tennis match cannot end in a draw, the events 'Sangeeta wins' and 'Reshma wins' are complementary:\nP(R) = 1 - P(S).\n\nSTEP-BY-STEP CALCULATION:\nP(R) = 1 - 0.62 = 0.38.\n\n[ROUGH_WORK]\n1 - 0.62 = 0.38.\nBoxed Answer: [ 0.38 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 202] Example 6: Savita and Hamida are friends. What is the probability that both will have (i) different birthdays? (ii) the same birthday? (ignoring a leap year).",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 202,
            "image_search_query": "two friends birthday different same probability 365",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Non-leap year has 365 days. Savita's birthday can be any of the 365 days.",
            "formula": "Total possible birthdays for Hamida = 365.\n(i) Different birthdays: Hamida's birthday can be any day except Savita's (364 days). P = 364 / 365.\n(ii) Same birthday: Hamida's birthday is on Savita's day (1 day). P = 1 - P(different) = 1/365.",
            "substitution": "(i) P = 364/365. (ii) P = 1/365.",
            "calculation": "(i) 364/365. (ii) 1/365.",
            "finalAnswer": "(i) 364/365, (ii) 1/365",
            "unit": "probability",
            "solution": "GIVEN:\nTwo friends Savita and Hamida. Non-leap year = 365 days.\n\nTO FIND:\n(i) Probability of different birthdays.\n(ii) Probability of the same birthday.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Different birthdays:\nOut of 365 days in a year, Savita's birthday is fixed on some day.\nFor Hamida to have a DIFFERENT birthday, her birthday can fall on any of the remaining (365 - 1) = 364 days.\nP(Different birthdays) = 364 / 365.\n\nPart (ii): Same birthday:\nThe event that both have the same birthday is the complement of having different birthdays:\nP(Same birthday) = 1 - P(Different birthdays)\nP(Same birthday) = 1 - (364 / 365) = 1 / 365.\n\n[ROUGH_WORK]\n364/365 and 1/365. Sum = 1.\nBoxed Answer: [ (i) 364/365, (ii) 1/365 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 203] Example 7: There are 40 students in Class X of a school of whom 25 are girls and 15 are boys. The class teacher has to select one student as a class representative. She writes the name of each student on a separate card, the cards being identical. Then she puts cards in a bag and stirs them thoroughly. She then draws one card from the bag. What is the probability that the name written on the card is the name of (i) a girl? (ii) a boy?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 203,
            "image_search_query": "class representative selection probability girls boys",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Total students = 40. Girls = 25. Boys = 15.",
            "formula": "P(E) = n(E) / n(S).",
            "substitution": "(i) P(Girl) = 25 / 40 = 5 / 8.\n(ii) P(Boy) = 15 / 40 = 3 / 8.",
            "calculation": "5/8 = 0.625. 3/8 = 0.375.",
            "finalAnswer": "(i) 5/8 (or 0.625), (ii) 3/8 (or 0.375)",
            "unit": "probability",
            "solution": "GIVEN:\nTotal students in Class X = 40 (n(S) = 40).\nNumber of girls = 25.\nNumber of boys = 15.\n\nTO FIND:\n(i) Probability that the chosen representative is a girl.\n(ii) Probability that the chosen representative is a boy.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): P(Girl) = 25 / 40\nDivide numerator and denominator by 5:\nP(Girl) = 5 / 8 = 0.625.\n\nPart (ii): P(Boy) = 15 / 40\nDivide numerator and denominator by 5:\nP(Boy) = 3 / 8 = 0.375.\n(Alternatively: 1 - 5/8 = 3/8).\n\n[ROUGH_WORK]\n25/40 = 5/8. 15/40 = 3/8. Sum = 1.\nBoxed Answer: [ (i) 5/8, (ii) 3/8 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 203] Example 8: A box contains 3 blue, 2 white, and 4 red marbles. If a marble is drawn at random from the box, what is the probability that it will be (i) white? (ii) blue? (iii) red?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 203,
            "image_search_query": "marbles box random draw probability blue white red",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Marbles: 3 blue, 2 white, 4 red. Total marbles = 3 + 2 + 4 = 9.",
            "formula": "P(E) = n(E) / n(S).",
            "substitution": "(i) White: 2/9. (ii) Blue: 3/9 = 1/3. (iii) Red: 4/9.",
            "calculation": "(i) 2/9. (ii) 3/9 = 1/3. (iii) 4/9. Sum = 2/9 + 3/9 + 4/9 = 9/9 = 1.",
            "finalAnswer": "(i) 2/9, (ii) 1/3, (iii) 4/9",
            "unit": "probability",
            "solution": "GIVEN:\nA box contains 3 blue, 2 white, and 4 red marbles.\nTotal marbles, n(S) = 3 + 2 + 4 = 9.\n\nTO FIND:\n(i) P(White), (ii) P(Blue), (iii) P(Red).\n\nSTEP-BY-STEP CALCULATION:\nPart (i): P(White) = Number of white marbles / Total marbles = 2 / 9.\nPart (ii): P(Blue) = Number of blue marbles / Total marbles = 3 / 9 = 1 / 3.\nPart (iii): P(Red) = Number of red marbles / Total marbles = 4 / 9.\n\n[ROUGH_WORK]\n2/9, 3/9 = 1/3, 4/9.\nBoxed Answer: [ (i) 2/9, (ii) 1/3, (iii) 4/9 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 204] Example 9: Harpreet tosses two different coins simultaneously (say, one is of ₹ 1 and other of ₹ 2). What is the probability that she gets at least one head?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 204,
            "image_search_query": "two coins simultaneously tossed at least one head",
            "has_diagram": True,
            "diagram_svg": svg_coins,
            "given": "Two coins tossed simultaneously. Sample space S = {(H,H), (H,T), (T,H), (T,T)}. Total outcomes n(S) = 4.",
            "formula": "At least one head = {HH, HT, TH} (3 outcomes). Alternatively: 1 - P(no heads) = 1 - P(TT).",
            "substitution": "Favourable outcomes = 3. Total outcomes = 4. P(At least one head) = 3 / 4.",
            "calculation": "3/4 = 0.75.",
            "finalAnswer": "3/4 (or 0.75)",
            "unit": "probability",
            "solution": "GIVEN:\nTwo different coins tossed simultaneously.\nSample space S = {(H, H), (H, T), (T, H), (T, T)}.\nTotal possible outcomes, n(S) = 4.\n\nTO FIND:\nProbability of getting at least one head.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Identify favourable outcomes:\n'At least one head' means 1 head or 2 heads.\nFavourable outcomes = {(H, H), (H, T), (T, H)}.\nNumber of favourable outcomes = 3.\n\nStep 2: Calculate probability:\nP(At least one head) = 3 / 4 = 0.75.\n\nAlternative Method:\nP(No heads) = P(T, T) = 1 / 4.\nP(At least one head) = 1 - P(No heads) = 1 - 1/4 = 3 / 4.\n\n[ROUGH_WORK]\n3/4 = 0.75.\nBoxed Answer: [ 3/4 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 204] Example 10: In a musical chair game, the person playing the music has been advised to stop playing the music at any time within 2 minutes after she starts playing. What is the probability that the music will stop within the first half-minute after starting?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 204,
            "image_search_query": "musical chair game continuous probability time interval",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Total time interval = 2 minutes. Target sub-interval = first half-minute = 0.5 minutes (or 1/2 minute).",
            "formula": "Geometric / Continuous Probability: P(E) = (Length of favourable interval) / (Total length of time interval).",
            "substitution": "Length of favourable interval = 0.5 minutes. Total interval = 2 minutes. P = 0.5 / 2 = 1 / 4.",
            "calculation": "0.5 / 2 = 1/4 = 0.25.",
            "finalAnswer": "1/4 (or 0.25)",
            "unit": "probability",
            "solution": "GIVEN:\nTotal time interval within which music can stop = 2 minutes (from t = 0 to t = 2).\nTarget event: Music stops within the first half-minute (from t = 0 to t = 0.5).\n\nTO FIND:\nProbability that the music stops within the first half-minute.\n\nFORMULA USED:\nGeometric Probability (Uniform Continuous Distribution):\nP(E) = (Length of favourable time interval) / (Total time interval length).\n\nSTEP-BY-STEP CALCULATION:\n- Length of favourable interval = 1/2 minute = 0.5 minute\n- Total interval length = 2 minutes\nP = (1 / 2) / 2 = 1 / 4 = 0.25.\n\n[ROUGH_WORK]\n0.5 / 2 = 1/4 = 0.25.\nBoxed Answer: [ 1/4 (or 0.25) ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 204] Example 11: A missing helicopter is reported to have crashed somewhere in the rectangular region shown in Fig. 14.2. What is the probability that it crashed inside the lake shown in the figure? (Rectangle dimensions: length = 9 km, breadth = 4.5 km; Lake dimensions: length = 2.5 km, breadth = 2 km).",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 204,
            "image_search_query": "helicopter crash lake rectangular area geometric probability",
            "has_diagram": True,
            "diagram_svg": svg_cards,
            "given": "Rectangular region: length = 9 km, width = 4.5 km. Total area = 9 × 4.5 = 40.5 km². Lake dimensions: length = 9 - 6 = 3 km (or 2.5 km), width = 4.5 - 2.5 = 2 km (Fig. 14.2). Lake area = 2.5 × 2 = 5 km².",
            "formula": "Geometric Probability: P(Crash in lake) = Area of lake / Total area of region.",
            "substitution": "Lake area = 5 km². Total area = 40.5 km² = 81/2 km². P = 5 / 40.5 = 50 / 405 = 10 / 81.",
            "calculation": "5 / 40.5 = 10 / 81.",
            "finalAnswer": "10/81",
            "unit": "probability",
            "solution": "GIVEN:\nEntire search area is a rectangle with length = 9 km and breadth = 4.5 km.\nTotal Area = 9 × 4.5 = 40.5 km².\nFrom Fig. 14.2, the lake has dimensions:\nLength = 9 - 6.5 = 2.5 km\nBreadth = 4.5 - 2.5 = 2 km.\nArea of Lake = 2.5 × 2 = 5 km².\n\nTO FIND:\nProbability that the helicopter crashed inside the lake.\n\nFORMULA USED:\nGeometric Probability:\nP(Crash in lake) = Area of Lake / Total Area.\n\nSTEP-BY-STEP CALCULATION:\nP = 5 / 40.5\nMultiply numerator and denominator by 10:\nP = 50 / 405\nDivide by 5:\nP = 10 / 81.\n\n[ROUGH_WORK]\n5 / 40.5 = 50 / 405 = 10 / 81 ≈ 0.1235.\nBoxed Answer: [ 10/81 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 205] Example 12: A carton consists of 100 shirts of which 88 are good, 8 have minor defects and 4 have major defects. Jimmy, a trader, will only accept the shirts which are good, but Sujatha, another trader, will only reject the shirts which have major defects. One shirt is drawn at random from the carton. What is the probability that (i) it is acceptable to Jimmy? (ii) it is acceptable to Sujatha?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 205,
            "image_search_query": "shirts carton defects traders jimmy sujatha probability",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Carton of 100 shirts: 88 good, 8 minor defects, 4 major defects. Total = 100.\nJimmy accepts only good shirts (88).\nSujatha rejects only major defects ⇒ accepts good + minor defects = 88 + 8 = 96.",
            "formula": "P(E) = n(E) / n(S).",
            "substitution": "(i) P(Jimmy accepts) = 88 / 100 = 0.88.\n(ii) P(Sujatha accepts) = 96 / 100 = 0.96.",
            "calculation": "88/100 = 0.88. 96/100 = 0.96.",
            "finalAnswer": "(i) 0.88, (ii) 0.96",
            "unit": "probability",
            "solution": "GIVEN:\nTotal shirts in carton, n(S) = 100.\n- Good shirts = 88\n- Minor defect shirts = 8\n- Major defect shirts = 4\n\nTO FIND:\n(i) Probability that the shirt is acceptable to Jimmy.\n(ii) Probability that the shirt is acceptable to Sujatha.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Acceptable to Jimmy:\nJimmy accepts ONLY good shirts.\nNumber of favourable shirts = 88.\nP(Jimmy) = 88 / 100 = 0.88.\n\nPart (ii): Acceptable to Sujatha:\nSujatha only rejects major defects, so she accepts good shirts AND shirts with minor defects.\nNumber of favourable shirts = 88 + 8 = 96 (or 100 - 4 = 96).\nP(Sujatha) = 96 / 100 = 0.96.\n\n[ROUGH_WORK]\n88/100 = 0.88. 96/100 = 0.96.\nBoxed Answer: [ (i) 0.88, (ii) 0.96 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 205] Example 13: Two dice, one blue and one grey, are thrown at the same time. Write down all the possible outcomes. What is the probability that the sum of the two numbers appearing on the top of the dice is (i) 8? (ii) 13? (iii) less than or equal to 12?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 205,
            "image_search_query": "two dice thrown sample space sum 8 13 12",
            "has_diagram": True,
            "diagram_svg": svg_dice,
            "given": "Two dice thrown simultaneously. Sample space S = {(1,1), (1,2), ..., (6,6)}. Total outcomes n(S) = 6 × 6 = 36.",
            "formula": "P(E) = n(E) / n(S).",
            "substitution": "(i) Sum = 8: {(2,6), (3,5), (4,4), (5,3), (6,2)} ⇒ 5 outcomes. P = 5/36.\n(ii) Sum = 13: Maximum possible sum is 6 + 6 = 12. Favourable outcomes = 0. P = 0/36 = 0 (Impossible event).\n(iii) Sum ≤ 12: All 36 outcomes have sum ≤ 12. Favourable outcomes = 36. P = 36/36 = 1 (Sure event).",
            "calculation": "(i) 5/36. (ii) 0. (iii) 1.",
            "finalAnswer": "(i) 5/36, (ii) 0, (iii) 1",
            "unit": "probability",
            "solution": "GIVEN:\nTwo dice (blue and grey) are thrown simultaneously.\nTotal elementary outcomes, n(S) = 6 × 6 = 36.\n\nTO FIND:\nProbability that the sum of the two numbers is:\n(i) 8\n(ii) 13\n(iii) Less than or equal to 12\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Sum = 8:\nFavourable pairs = {(2, 6), (3, 5), (4, 4), (5, 3), (6, 2)}.\nNumber of favourable outcomes = 5.\nP(Sum = 8) = 5 / 36.\n\nPart (ii): Sum = 13:\nThe maximum possible numbers on two dice are 6 and 6, whose maximum sum is 6 + 6 = 12.\nA sum of 13 is impossible.\nNumber of favourable outcomes = 0.\nP(Sum = 13) = 0 / 36 = 0 (Impossible Event).\n\nPart (iii): Sum ≤ 12:\nEvery pair (a, b) on two dice satisfies 1 + 1 = 2 ≤ a + b ≤ 6 + 6 = 12.\nAll 36 outcomes satisfy this condition.\nP(Sum ≤ 12) = 36 / 36 = 1 (Sure Event).\n\n[ROUGH_WORK]\nSum=8 has 5 pairs. Sum=13 has 0 pairs. Sum<=12 has all 36 pairs.\nBoxed Answer: [ (i) 5/36, (ii) 0, (iii) 1 ].",
            "concept_questions": []
        }
    ]

    m3_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 206] Exercise 14.1 Q5: If P(E) = 0.05, what is the probability of 'not E'?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 206,
            "image_search_query": "complementary probability not e subtraction formula",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "P(E) = 0.05.",
            "formula": "P(not E) = 1 - P(E).",
            "substitution": "P(not E) = 1 - 0.05 = 0.95.",
            "calculation": "1.00 - 0.05 = 0.95.",
            "finalAnswer": "0.95",
            "unit": "probability",
            "solution": "GIVEN:\nP(E) = 0.05.\n\nTO FIND:\nProbability of 'not E', denoted P(Ē).\n\nFORMULA USED:\nP(E) + P(not E) = 1\nP(not E) = 1 - P(E).\n\nSTEP-BY-STEP CALCULATION:\nP(not E) = 1 - 0.05 = 0.95.\n\n[ROUGH_WORK]\n1.00 - 0.05 = 0.95.\nBoxed Answer: [ 0.95 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 206] Exercise 14.1 Q6: A bag contains lemon flavoured candies only. Malini takes out one candy without looking into the bag. What is the probability that she takes out (i) an orange flavoured candy? (ii) a lemon flavoured candy?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 206,
            "image_search_query": "impossible sure event candies bag probability",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Bag contains ONLY lemon-flavoured candies.",
            "formula": "P(impossible event) = 0; P(sure event) = 1.",
            "substitution": "(i) No orange candies in bag ⇒ P(orange candy) = 0.\n(ii) All candies in bag are lemon ⇒ P(lemon candy) = 1.",
            "calculation": "(i) 0. (ii) 1.",
            "finalAnswer": "(i) 0, (ii) 1",
            "unit": "probability",
            "solution": "GIVEN:\nA bag contains only lemon flavoured candies.\n\nTO FIND:\n(i) Probability of taking out an orange flavoured candy.\n(ii) Probability of taking out a lemon flavoured candy.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Orange flavoured candy:\nThere are zero orange flavoured candies in the bag.\nThis is an IMPOSSIBLE EVENT.\nP(Orange candy) = 0.\n\nPart (ii): Lemon flavoured candy:\nEvery candy in the bag is lemon flavoured.\nDrawing a lemon candy is guaranteed (a SURE/CERTAIN EVENT).\nP(Lemon candy) = 1.\n\n[ROUGH_WORK]\nImpossible = 0; Sure = 1.\nBoxed Answer: [ (i) 0, (ii) 1 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 207] Exercise 14.1 Q7: It is given that in a group of 3 students, the probability of 2 students not having the same birthday is 0.992. What is the probability that the 2 students have the same birthday?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 207,
            "image_search_query": "complementary birthday probability subtraction",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "P(2 students not having same birthday) = 0.992.",
            "formula": "P(same birthday) = 1 - P(not same birthday).",
            "substitution": "P(same birthday) = 1 - 0.992 = 0.008.",
            "calculation": "1.000 - 0.992 = 0.008.",
            "finalAnswer": "0.008",
            "unit": "probability",
            "solution": "GIVEN:\nProbability of 2 students not having the same birthday, P(Ē) = 0.992.\n\nTO FIND:\nProbability of the 2 students having the same birthday, P(E).\n\nFORMULA USED:\nP(E) + P(Ē) = 1\nP(E) = 1 - P(Ē).\n\nSTEP-BY-STEP CALCULATION:\nP(Same birthday) = 1 - 0.992\n= 0.008.\n\n[ROUGH_WORK]\n1.000 - 0.992 = 0.008.\nBoxed Answer: [ 0.008 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 207] Exercise 14.1 Q8: A bag contains 3 red balls and 5 black balls. A ball is drawn at random from the bag. What is the probability that the ball drawn is (i) red? (ii) not red?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 207,
            "image_search_query": "red black balls probability bag random draw",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Bag has 3 red and 5 black balls. Total balls n(S) = 3 + 5 = 8.",
            "formula": "P(Red) = n(Red) / n(S). P(not Red) = 1 - P(Red).",
            "substitution": "(i) P(Red) = 3 / 8.\n(ii) P(not Red) = 1 - 3/8 = 5 / 8.",
            "calculation": "3/8 = 0.375. 5/8 = 0.625.",
            "finalAnswer": "(i) 3/8, (ii) 5/8",
            "unit": "probability",
            "solution": "GIVEN:\nNumber of red balls = 3.\nNumber of black balls = 5.\nTotal balls in the bag, n(S) = 3 + 5 = 8.\n\nTO FIND:\n(i) P(Red), (ii) P(not Red).\n\nSTEP-BY-STEP CALCULATION:\nPart (i): P(Red) = Number of red balls / Total balls = 3 / 8.\nPart (ii): P(not Red) = 1 - P(Red) = 1 - 3/8 = 5 / 8.\n(Alternatively: not red = black balls = 5; P = 5/8).\n\n[ROUGH_WORK]\n3/8 and 5/8. Sum = 1.\nBoxed Answer: [ (i) 3/8, (ii) 5/8 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 207] Exercise 14.1 Q9: A box contains 5 red marbles, 8 white marbles and 4 green marbles. One marble is taken out of the box at random. What is the probability that the marble taken out will be (i) red? (ii) white? (iii) not green?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 207,
            "image_search_query": "red white green marbles probability not green",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "5 red, 8 white, 4 green marbles. Total marbles = 5 + 8 + 4 = 17.",
            "formula": "P(E) = n(E) / n(S). P(not green) = (Red + White) / Total = 1 - P(Green).",
            "substitution": "(i) P(Red) = 5 / 17.\n(ii) P(White) = 8 / 17.\n(iii) P(not Green) = (5 + 8) / 17 = 13 / 17.",
            "calculation": "(i) 5/17. (ii) 8/17. (iii) 13/17.",
            "finalAnswer": "(i) 5/17, (ii) 8/17, (iii) 13/17",
            "unit": "probability",
            "solution": "GIVEN:\nRed marbles = 5\nWhite marbles = 8\nGreen marbles = 4\nTotal marbles, n(S) = 5 + 8 + 4 = 17.\n\nTO FIND:\n(i) P(Red), (ii) P(White), (iii) P(not Green).\n\nSTEP-BY-STEP CALCULATION:\nPart (i): P(Red) = 5 / 17.\nPart (ii): P(White) = 8 / 17.\nPart (iii): P(not Green) = P(Red or White) = (5 + 8) / 17 = 13 / 17.\n(Alternatively: 1 - P(Green) = 1 - 4/17 = 13/17).\n\n[ROUGH_WORK]\n5/17, 8/17, 13/17.\nBoxed Answer: [ (i) 5/17, (ii) 8/17, (iii) 13/17 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 207] Exercise 14.1 Q10: A piggy bank contains hundred 50p coins, fifty ₹ 1 coins, twenty ₹ 2 coins and ten ₹ 5 coins. If it is equally likely that one of the coins will fall out when the bank is turned upside down, what is the probability that the coin (i) will be a 50 p coin? (ii) will not be a ₹ 5 coin?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 207,
            "image_search_query": "piggy bank coins random fall probability",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Coins in piggy bank: 100 of 50p, 50 of ₹1, 20 of ₹2, 10 of ₹5. Total coins n(S) = 100 + 50 + 20 + 10 = 180.",
            "formula": "P(E) = n(E) / n(S). P(not ₹5) = 1 - P(₹5).",
            "substitution": "(i) P(50p coin) = 100 / 180 = 10 / 18 = 5 / 9.\n(ii) P(not ₹5) = (180 - 10) / 180 = 170 / 180 = 17 / 18.",
            "calculation": "(i) 5/9. (ii) 17/18.",
            "finalAnswer": "(i) 5/9, (ii) 17/18",
            "unit": "probability",
            "solution": "GIVEN:\nComposition of coins in the piggy bank:\n- 50p coins = 100\n- ₹ 1 coins = 50\n- ₹ 2 coins = 20\n- ₹ 5 coins = 10\nTotal coins, n(S) = 100 + 50 + 20 + 10 = 180.\n\nTO FIND:\n(i) Probability that the coin is a 50p coin.\n(ii) Probability that the coin will not be a ₹ 5 coin.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): P(50p coin):\nNumber of 50p coins = 100.\nP(50p) = 100 / 180 = 10 / 18 = 5 / 9.\n\nPart (ii): P(not a ₹ 5 coin):\nNumber of coins that are NOT ₹ 5 = 180 - 10 = 170.\nP(not ₹ 5) = 170 / 180 = 17 / 18.\n(Alternatively: 1 - P(₹ 5) = 1 - 10/180 = 1 - 1/18 = 17/18).\n\n[ROUGH_WORK]\n100/180 = 5/9. 170/180 = 17/18.\nBoxed Answer: [ (i) 5/9, (ii) 17/18 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 207] Exercise 14.1 Q11: Gopi buys a fish from a shop for his aquarium. The shopkeeper takes out one fish at random from a tank containing 5 male fish and 8 female fish (see Fig. 14.4). What is the probability that the fish taken out is a male fish?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 207,
            "image_search_query": "gopi aquarium fish shopkeeper male probability",
            "has_diagram": True,
            "diagram_svg": svg_cards,
            "given": "Tank has 5 male fish and 8 female fish (Fig. 14.4). Total fish n(S) = 5 + 8 = 13.",
            "formula": "P(Male fish) = Number of male fish / Total fish.",
            "substitution": "P = 5 / 13.",
            "calculation": "5 / 13 ≈ 0.385.",
            "finalAnswer": "5/13",
            "unit": "probability",
            "solution": "GIVEN:\nNumber of male fish = 5.\nNumber of female fish = 8.\nTotal fish in the tank, n(S) = 5 + 8 = 13 (Fig. 14.4).\n\nTO FIND:\nProbability that the fish taken out is a male fish.\n\nFORMULA USED:\nP(Male fish) = Number of male fish / Total fish in tank.\n\nSTEP-BY-STEP CALCULATION:\nP(Male fish) = 5 / 13.\n\n[ROUGH_WORK]\n5 / 13.\nBoxed Answer: [ 5/13 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 207] Exercise 14.1 Q12: A game of chance consists of spinning an arrow which comes to rest pointing at one of the numbers 1, 2, 3, 4, 5, 6, 7, 8 (see Fig. 14.5), and these are equally likely outcomes. What is the probability that it will point at (i) 8? (ii) an odd number? (iii) a number greater than 2? (iv) a number less than 9?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 207,
            "image_search_query": "spinning arrow spinner game numbers 1 to 8 probability",
            "has_diagram": True,
            "diagram_svg": svg_cards,
            "given": "Spinner with 8 equally likely sectors: 1, 2, 3, 4, 5, 6, 7, 8 (Fig. 14.5). Total outcomes n(S) = 8.",
            "formula": "P(E) = n(E) / n(S).",
            "substitution": "(i) Number 8: {8} ⇒ 1/8.\n(ii) Odd numbers: {1, 3, 5, 7} ⇒ 4/8 = 1/2.\n(iii) Number > 2: {3, 4, 5, 6, 7, 8} ⇒ 6/8 = 3/4.\n(iv) Number < 9: {1, 2, 3, 4, 5, 6, 7, 8} ⇒ 8/8 = 1.",
            "calculation": "(i) 1/8. (ii) 4/8 = 1/2. (iii) 6/8 = 3/4. (iv) 8/8 = 1.",
            "finalAnswer": "(i) 1/8, (ii) 1/2, (iii) 3/4, (iv) 1",
            "unit": "probability",
            "solution": "GIVEN:\nA spinning arrow pointing at numbers 1, 2, 3, 4, 5, 6, 7, 8 (Fig. 14.5).\nTotal possible outcomes, n(S) = 8 (equally likely).\n\nTO FIND:\nProbability of pointing at:\n(i) 8\n(ii) An odd number\n(iii) A number greater than 2\n(iv) A number less than 9\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Pointing at 8:\nFavourable outcome = {8} (1 outcome).\nP(8) = 1 / 8.\n\nPart (ii): Pointing at an odd number:\nOdd numbers in set = {1, 3, 5, 7} (4 outcomes).\nP(Odd) = 4 / 8 = 1 / 2.\n\nPart (iii): Pointing at a number greater than 2:\nNumbers > 2 = {3, 4, 5, 6, 7, 8} (6 outcomes).\nP(Number > 2) = 6 / 8 = 3 / 4.\n\nPart (iv): Pointing at a number less than 9:\nAll 8 numbers are less than 9: {1, 2, 3, 4, 5, 6, 7, 8} (8 outcomes).\nP(Number < 9) = 8 / 8 = 1 (Sure Event).\n\n[ROUGH_WORK]\n1/8, 4/8=1/2, 6/8=3/4, 8/8=1.\nBoxed Answer: [ (i) 1/8, (ii) 1/2, (iii) 3/4, (iv) 1 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 207] Exercise 14.1 Q13: A die is thrown once. Find the probability of getting (i) a prime number; (ii) a number lying between 2 and 6; (iii) an odd number.",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 207,
            "image_search_query": "die thrown prime between 2 6 odd probability",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "A single die thrown once. Sample space S = {1, 2, 3, 4, 5, 6}. Total outcomes n(S) = 6.",
            "formula": "P(E) = n(E) / n(S).",
            "substitution": "(i) Prime numbers: {2, 3, 5} ⇒ 3 outcomes. P = 3/6 = 1/2.\n(ii) Between 2 and 6: {3, 4, 5} ⇒ 3 outcomes. P = 3/6 = 1/2.\n(iii) Odd numbers: {1, 3, 5} ⇒ 3 outcomes. P = 3/6 = 1/2.",
            "calculation": "(i) 3/6 = 1/2. (ii) 3/6 = 1/2. (iii) 3/6 = 1/2.",
            "finalAnswer": "(i) 1/2, (ii) 1/2, (iii) 1/2",
            "unit": "probability",
            "solution": "GIVEN:\nA fair die is thrown once.\nSample space S = {1, 2, 3, 4, 5, 6}.\nTotal outcomes, n(S) = 6.\n\nTO FIND:\n(i) P(Prime number), (ii) P(Number between 2 and 6), (iii) P(Odd number).\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Prime number:\nPrime numbers on a die are 2, 3, and 5 (Note: 1 is neither prime nor composite).\nFavourable outcomes = {2, 3, 5} (3 outcomes).\nP(Prime) = 3 / 6 = 1 / 2.\n\nPart (ii): Number lying between 2 and 6:\nStrictly between 2 and 6 means {3, 4, 5} (3 outcomes).\nP(Between 2 and 6) = 3 / 6 = 1 / 2.\n\nPart (iii): Odd number:\nOdd numbers on a die are {1, 3, 5} (3 outcomes).\nP(Odd) = 3 / 6 = 1 / 2.\n\n[ROUGH_WORK]\nEach case has 3 favourable outcomes out of 6: 3/6 = 1/2.\nBoxed Answer: [ (i) 1/2, (ii) 1/2, (iii) 1/2 ].",
            "concept_questions": []
        }
    ]

    m4_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 207] Exercise 14.1 Q14: One card is drawn from a well-shuffled deck of 52 cards. Find the probability of getting:\n(i) a king of red colour\n(ii) a face card\n(iii) a red face card\n(iv) the jack of hearts\n(v) a spade\n(vi) the queen of diamonds",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 207,
            "image_search_query": "52 cards king face card spade queen diamonds probability",
            "has_diagram": True,
            "diagram_svg": svg_cards,
            "given": "Standard well-shuffled deck of 52 cards. Total cards n(S) = 52.",
            "formula": "P(E) = n(E) / n(S).",
            "substitution": "(i) Kings of red colour: King of Hearts, King of Diamonds ⇒ 2 cards. P = 2/52 = 1/26.\n(ii) Face cards: Jacks, Queens, Kings across 4 suits = 4 × 3 = 12 cards. P = 12/52 = 3/13.\n(iii) Red face cards: 2 suits (Hearts, Diamonds) × 3 = 6 cards. P = 6/52 = 3/26.\n(iv) Jack of hearts: Exactly 1 card. P = 1/52.\n(v) A spade: 13 cards in spades suit. P = 13/52 = 1/4.\n(vi) Queen of diamonds: Exactly 1 card. P = 1/52.",
            "calculation": "(i) 1/26, (ii) 3/13, (iii) 3/26, (iv) 1/52, (v) 1/4, (vi) 1/52.",
            "finalAnswer": "(i) 1/26, (ii) 3/13, (iii) 3/26, (iv) 1/52, (v) 1/4, (vi) 1/52",
            "unit": "probability",
            "solution": "GIVEN:\nA standard deck of 52 playing cards (n(S) = 52).\n\nTO FIND:\nProbabilities for each of the 6 card events.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): A king of red colour:\nThere are 2 red kings: King of Hearts and King of Diamonds.\nP(Red King) = 2 / 52 = 1 / 26.\n\nPart (ii): A face card:\nFace cards are Jacks, Queens, and Kings (3 per suit × 4 suits = 12 cards).\nP(Face Card) = 12 / 52 = 3 / 13.\n\nPart (iii): A red face card:\nRed suits are Hearts and Diamonds (3 face cards each = 6 red face cards).\nP(Red Face Card) = 6 / 52 = 3 / 26.\n\nPart (iv): The jack of hearts:\nThere is only 1 Jack of Hearts in the entire deck.\nP(Jack of Hearts) = 1 / 52.\n\nPart (v): A spade:\nThere are 13 spades in the deck.\nP(Spade) = 13 / 52 = 1 / 4.\n\nPart (vi): The queen of diamonds:\nThere is only 1 Queen of Diamonds in the deck.\nP(Queen of Diamonds) = 1 / 52.\n\n[ROUGH_WORK]\n2/52=1/26, 12/52=3/13, 6/52=3/26, 1/52, 13/52=1/4, 1/52.\nBoxed Answer: [ (i) 1/26, (ii) 3/13, (iii) 3/26, (iv) 1/52, (v) 1/4, (vi) 1/52 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 208] Exercise 14.1 Q15: Five cards—the ten, jack, queen, king and ace of diamonds, are well-shuffled with their face downwards. One card is then picked up at random.\n(i) What is the probability that the card is the queen?\n(ii) If the queen is drawn and put aside, what is the probability that the second card picked up is (a) an ace? (b) a queen?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 208,
            "image_search_query": "five diamonds cards without replacement probability",
            "has_diagram": True,
            "diagram_svg": svg_cards,
            "given": "Five cards: 10, Jack, Queen, King, Ace of Diamonds. Initial total = 5.",
            "formula": "P(E) = n(E) / n(S). Without replacement: total decreases to 4.",
            "substitution": "(i) Queen: 1 / 5.\n(ii) Queen is put aside ⇒ remaining cards = {10, J, K, A} (4 cards).\n(a) An ace: 1 / 4.\n(b) A queen: 0 / 4 = 0.",
            "calculation": "(i) 1/5. (ii)(a) 1/4. (ii)(b) 0.",
            "finalAnswer": "(i) 1/5, (ii)(a) 1/4, (ii)(b) 0",
            "unit": "probability",
            "solution": "GIVEN:\nInitial set of 5 cards: {10, Jack, Queen, King, Ace} of Diamonds.\nTotal initial cards, n(S) = 5.\n\nTO FIND:\n(i) Probability that the chosen card is the queen.\n(ii) If the queen is drawn and kept aside, probability that the next card is (a) an ace, (b) a queen.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): P(Queen):\nThere is 1 queen among the 5 cards.\nP(Queen) = 1 / 5.\n\nPart (ii): The queen is put aside:\nRemaining cards in the deck: {10, Jack, King, Ace}.\nTotal remaining cards = 4.\n(a) Probability of an Ace:\nThere is 1 ace among the remaining 4 cards.\nP(Ace) = 1 / 4.\n\n(b) Probability of a Queen:\nSince the queen was already removed, there are 0 queens remaining.\nP(Queen) = 0 / 4 = 0 (Impossible Event).\n\n[ROUGH_WORK]\n1/5. Without replacement: n=4. Ace = 1/4. Queen = 0/4 = 0.\nBoxed Answer: [ (i) 1/5, (ii)(a) 1/4, (ii)(b) 0 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 208] Exercise 14.1 Q16: 12 defective pens are accidentally mixed with 132 good ones. It is not possible to just look at a pen and tell whether or not it is defective. One pen is taken out at random from this lot. Determine the probability that the pen taken out is a good one.",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 208,
            "image_search_query": "defective pens mixed good ones probability",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Defective pens = 12. Good pens = 132. Total pens n(S) = 12 + 132 = 144.",
            "formula": "P(Good pen) = Number of good pens / Total pens.",
            "substitution": "P = 132 / 144 = 11 / 12.",
            "calculation": "Divide by 12: 132 / 12 = 11; 144 / 12 = 12. P = 11 / 12 ≈ 0.9167.",
            "finalAnswer": "11/12",
            "unit": "probability",
            "solution": "GIVEN:\nNumber of defective pens = 12.\nNumber of good pens = 132.\nTotal number of pens in the lot, n(S) = 12 + 132 = 144.\n\nTO FIND:\nProbability that a randomly drawn pen is a good one.\n\nFORMULA USED:\nP(Good pen) = Number of good pens / Total pens.\n\nSTEP-BY-STEP CALCULATION:\nP(Good pen) = 132 / 144.\nDivide both numerator and denominator by 12:\n132 / 12 = 11\n144 / 12 = 12\nP(Good pen) = 11 / 12.\n\n[ROUGH_WORK]\n132/144 = 11/12.\nBoxed Answer: [ 11/12 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 208] Exercise 14.1 Q17: (i) A lot of 20 bulbs contain 4 defective ones. One bulb is drawn at random from the lot. What is the probability that this bulb is defective?\n(ii) Suppose the bulb drawn in (i) is not defective and is not replaced. Now one bulb is drawn at random from the rest. What is the probability that this bulb is not defective?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 208,
            "image_search_query": "defective bulbs without replacement conditional probability",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Total bulbs = 20. Defective = 4, Non-defective (good) = 16.",
            "formula": "P(E) = n(E) / n(S). Without replacement of a good bulb: Total = 19, Good = 15.",
            "substitution": "(i) P(Defective) = 4 / 20 = 1 / 5 = 0.2.\n(ii) 1 non-defective bulb removed and not replaced ⇒ Total bulbs = 19, Non-defective = 16 - 1 = 15.\nP(not defective) = 15 / 19.",
            "calculation": "(i) 4/20 = 1/5. (ii) 15/19.",
            "finalAnswer": "(i) 1/5, (ii) 15/19",
            "unit": "probability",
            "solution": "GIVEN:\nTotal bulbs in lot = 20.\nDefective bulbs = 4.\nNon-defective (good) bulbs = 20 - 4 = 16.\n\nTO FIND:\n(i) Probability that the drawn bulb is defective.\n(ii) If a non-defective bulb is drawn and not replaced, probability that the second bulb drawn is not defective.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Initial draw:\nTotal bulbs = 20, Defective bulbs = 4.\nP(Defective) = 4 / 20 = 1 / 5 = 0.2.\n\nPart (ii): Second draw without replacement:\nA non-defective bulb was drawn and set aside.\n- Remaining non-defective bulbs = 16 - 1 = 15\n- Remaining defective bulbs = 4\n- Total remaining bulbs in the lot = 20 - 1 = 19.\nP(Not defective) = 15 / 19.\n\n[ROUGH_WORK]\n4/20 = 1/5. After 1 good bulb removed: 15/19.\nBoxed Answer: [ (i) 1/5, (ii) 15/19 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 208] Exercise 14.1 Q18: A box contains 90 discs which are numbered from 1 to 90. If one disc is drawn at random from the box, find the probability that it bears (i) a two-digit number (ii) a perfect square number (iii) a number divisible by 5.",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 208,
            "image_search_query": "numbered discs 1 to 90 two digit perfect square divisible by 5",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "90 discs numbered 1 to 90. Total discs n(S) = 90.",
            "formula": "P(E) = n(E) / n(S).",
            "substitution": "(i) Two-digit numbers: 10 to 90 ⇒ (90 - 10 + 1) = 81 discs. P = 81 / 90 = 9 / 10.\n(ii) Perfect squares: 1, 4, 9, 16, 25, 36, 49, 64, 81 ⇒ 9 discs. P = 9 / 90 = 1 / 10.\n(iii) Divisible by 5: 5, 10, 15, ..., 90 ⇒ 90 / 5 = 18 discs. P = 18 / 90 = 1 / 5.",
            "calculation": "(i) 81/90 = 9/10 = 0.9. (ii) 9/90 = 1/10 = 0.1. (iii) 18/90 = 1/5 = 0.2.",
            "finalAnswer": "(i) 9/10, (ii) 1/10, (iii) 1/5",
            "unit": "probability",
            "solution": "GIVEN:\nA box contains 90 discs numbered 1 to 90.\nTotal outcomes, n(S) = 90.\n\nTO FIND:\nProbability that the drawn disc bears:\n(i) A two-digit number\n(ii) A perfect square number\n(iii) A number divisible by 5\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Two-digit numbers:\nSingle-digit numbers are 1 through 9 (9 numbers).\nTwo-digit numbers are from 10 to 90 = 90 - 9 = 81 numbers.\nP(Two-digit number) = 81 / 90 = 9 / 10 = 0.9.\n\nPart (ii): Perfect square numbers:\nSquares between 1 and 90: {1²=1, 2²=4, 3²=9, 4²=16, 5²=25, 6²=36, 7²=49, 8²=64, 9²=81}.\nTotal perfect squares = 9.\nP(Perfect square) = 9 / 90 = 1 / 10 = 0.1.\n\nPart (iii): Numbers divisible by 5:\nMultiples of 5 from 1 to 90: {5, 10, 15, ..., 90}.\nNumber of multiples = 90 / 5 = 18.\nP(Divisible by 5) = 18 / 90 = 1 / 5 = 0.2.\n\n[ROUGH_WORK]\n81/90 = 9/10. 9/90 = 1/10. 18/90 = 1/5.\nBoxed Answer: [ (i) 9/10, (ii) 1/10, (iii) 1/5 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 208] Exercise 14.1 Q19: A child has a die whose six faces show the letters as given below: A, B, C, D, E, A. The die is thrown once. What is the probability of getting (i) A? (ii) D?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 208,
            "image_search_query": "letter die faces a b c d e a probability",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Six-faced die with letters: A, B, C, D, E, A. Total faces n(S) = 6.",
            "formula": "P(E) = n(E) / n(S).",
            "substitution": "(i) Letter A appears on 2 faces: {Face 1, Face 6}. P(A) = 2 / 6 = 1 / 3.\n(ii) Letter D appears on 1 face: {Face 4}. P(D) = 1 / 6.",
            "calculation": "(i) 2/6 = 1/3. (ii) 1/6.",
            "finalAnswer": "(i) 1/3, (ii) 1/6",
            "unit": "probability",
            "solution": "GIVEN:\nA die with 6 faces displaying: A, B, C, D, E, A.\nTotal possible outcomes, n(S) = 6.\n\nTO FIND:\n(i) Probability of getting 'A'.\n(ii) Probability of getting 'D'.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Getting 'A':\nLetter 'A' appears on 2 faces.\nNumber of favourable outcomes = 2.\nP(A) = 2 / 6 = 1 / 3.\n\nPart (ii): Getting 'D':\nLetter 'D' appears on 1 face.\nNumber of favourable outcomes = 1.\nP(D) = 1 / 6.\n\n[ROUGH_WORK]\n2/6 = 1/3. 1/6.\nBoxed Answer: [ (i) 1/3, (ii) 1/6 ].",
            "concept_questions": []
        }
    ]

    m5_worked_examples = [
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 208] Exercise 14.1 Q20: Suppose you drop a die at random on the rectangular region shown in Fig. 14.6. What is the probability that it will land inside the circle with diameter 1 m? (Rectangle dimensions: length = 3 m, breadth = 2 m).",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 208,
            "image_search_query": "drop die rectangle circle target geometric probability",
            "has_diagram": True,
            "diagram_svg": svg_cards,
            "given": "Rectangular region: length = 3 m, breadth = 2 m (Fig. 14.6). Circle inside: diameter d = 1 m ⇒ radius r = 0.5 m = 1/2 m.",
            "formula": "Geometric Probability: P = Area of circle / Total area of rectangle.",
            "substitution": "Area of rectangle = 3 × 2 = 6 m².\nArea of circle = πr² = π(1/2)² = π / 4 m².\nP = (π / 4) / 6 = π / 24.",
            "calculation": "P = π / 24.",
            "finalAnswer": "π/24",
            "unit": "probability",
            "solution": "GIVEN:\nA rectangular target region of length = 3 m and breadth = 2 m (Fig. 14.6).\nA circular region inside with diameter d = 1 m ⇒ radius, r = 1/2 m = 0.5 m.\n\nTO FIND:\nProbability that a dropped die lands inside the circle.\n\nFORMULA USED:\nGeometric Probability:\nP(Lands in circle) = Area of Circle / Area of Rectangle.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Compute total area of rectangle:\nArea_rectangle = length × breadth = 3 × 2 = 6 m².\n\nStep 2: Compute area of circular target:\nArea_circle = πr² = π × (1 / 2)² = π / 4 m².\n\nStep 3: Calculate Probability:\nP = Area_circle / Area_rectangle\nP = (π / 4) / 6 = π / 24.\n(In decimal using π ≈ 3.1416: P ≈ 3.1416 / 24 ≈ 0.131).\n\n[ROUGH_WORK]\n(π/4) / 6 = π / 24.\nBoxed Answer: [ π/24 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 208] Exercise 14.1 Q21: A lot consists of 144 ball pens of which 20 are defective and the others are good. Nuri will buy a pen if it is good, but will not buy if it is defective. The shopkeeper draws one pen at random and gives it to her. What is the probability that (i) She will buy it? (ii) She will not buy it?",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 208,
            "image_search_query": "ball pens defective good nuri buys probability",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Total pens = 144. Defective pens = 20. Good pens = 144 - 20 = 124. Nuri buys if good, refuses if defective.",
            "formula": "P(buys) = P(good pen) = 124 / 144. P(will not buy) = P(defective pen) = 20 / 144.",
            "substitution": "(i) 124 / 144 = 31 / 36.\n(ii) 20 / 144 = 5 / 36.",
            "calculation": "(i) 31/36. (ii) 5/36. Sum = 31/36 + 5/36 = 1.",
            "finalAnswer": "(i) 31/36, (ii) 5/36",
            "unit": "probability",
            "solution": "GIVEN:\nTotal ball pens in lot, n(S) = 144.\nNumber of defective pens = 20.\nNumber of good pens = 144 - 20 = 124.\n\nTO FIND:\n(i) Probability that Nuri buys the pen (i.e., pen is good).\n(ii) Probability that Nuri does not buy the pen (i.e., pen is defective).\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Probability she will buy it:\nShe buys only if the pen is good.\nP(Buys) = Number of good pens / Total pens\nP(Buys) = 124 / 144.\nDivide numerator and denominator by 4:\n124 / 4 = 31\n144 / 4 = 36\nP(Buys) = 31 / 36.\n\nPart (ii): Probability she will not buy it:\nShe will not buy if the pen is defective.\nP(Does not buy) = Number of defective pens / Total pens\nP(Does not buy) = 20 / 144 = 5 / 36.\n(Alternatively: 1 - 31/36 = 5/36).\n\n[ROUGH_WORK]\n124/144 = 31/36. 20/144 = 5/36.\nBoxed Answer: [ (i) 31/36, (ii) 5/36 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 208] Exercise 14.1 Q22: Refer to Example 13. (i) Complete the following table for the sum of two dice (Sums: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12). (ii) A student argues that 'there are 11 possible outcomes 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 and 12. Therefore, each of them has a probability 1/11.' Do you agree with this argument? Justify your answer.",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 208,
            "image_search_query": "two dice sum table fallacy 1 11 argument",
            "has_diagram": True,
            "diagram_svg": svg_dice,
            "given": "Two dice thrown. Total outcomes = 36. Possible sums range from 2 to 12.",
            "formula": "P(Sum = s) = (Number of pairs summing to s) / 36.",
            "substitution": "Sums and counts:\nSum 2: (1,1) ⇒ 1/36\nSum 3: (1,2), (2,1) ⇒ 2/36\nSum 4: (1,3), (2,2), (3,1) ⇒ 3/36\nSum 5: (1,4), (2,3), (3,2), (4,1) ⇒ 4/36\nSum 6: (1,5), (2,4), (3,3), (4,2), (5,1) ⇒ 5/36\nSum 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) ⇒ 6/36\nSum 8: (2,6), (3,5), (4,4), (5,3), (6,2) ⇒ 5/36\nSum 9: (3,6), (4,5), (5,4), (6,3) ⇒ 4/36\nSum 10: (4,6), (5,5), (6,4) ⇒ 3/36\nSum 11: (5,6), (6,5) ⇒ 2/36\nSum 12: (6,6) ⇒ 1/36.\nStudent argument: The 11 sums are NOT equally likely, so probability is NOT 1/11.",
            "calculation": "Probabilities range from 1/36 (for 2 and 12) to 6/36 (for 7). Student argument is false.",
            "finalAnswer": "(i) Table completed: [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]; (ii) Disagree, the 11 outcomes are not equally likely",
            "unit": "probability table",
            "solution": "GIVEN:\nTwo dice thrown simultaneously (36 total outcomes).\nSums range from 2 to 12.\n\nTO DO:\n(i) Complete the probability table for each sum.\n(ii) Analyze whether the 11 sums are equally likely with probability 1/11.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): Compute probabilities for each sum out of 36:\n- Sum 2: {(1,1)} → 1 / 36\n- Sum 3: {(1,2), (2,1)} → 2 / 36\n- Sum 4: {(1,3), (2,2), (3,1)} → 3 / 36\n- Sum 5: {(1,4), (2,3), (3,2), (4,1)} → 4 / 36\n- Sum 6: {(1,5), (2,4), (3,3), (4,2), (5,1)} → 5 / 36\n- Sum 7: {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)} → 6 / 36\n- Sum 8: {(2,6), (3,5), (4,4), (5,3), (6,2)} → 5 / 36\n- Sum 9: {(3,6), (4,5), (5,4), (6,3)} → 4 / 36\n- Sum 10: {(4,6), (5,5), (6,4)} → 3 / 36\n- Sum 11: {(5,6), (6,5)} → 2 / 36\n- Sum 12: {(6,6)} → 1 / 36\n\nPart (ii): Critique of the student's argument:\nI DO NOT AGREE with the student's argument.\nJustification: The 11 possible sums are NOT equally likely outcomes. For example, sum 7 can occur in 6 different ways (probability 6/36 = 1/6), whereas sum 2 can occur in only 1 way (probability 1/36). Since the elementary outcomes composing each sum are unequal in count, the probability of each sum is not 1/11.\n\n[ROUGH_WORK]\nPeak at sum 7 (6/36). Tails at 2 and 12 (1/36). Unequal chances ⇒ Not 1/11.\nBoxed Answer: [ Disagree; the 11 sums are not equally likely ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 209] Exercise 14.1 Q23: A game consists of tossing a one rupee coin 3 times and noting its outcome each time. Hanif wins if all the tosses give the same result i.e., three heads or three tails, and loses otherwise. Calculate the probability that Hanif will lose the game.",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 209,
            "image_search_query": "coin tossed 3 times hanif wins loses probability",
            "has_diagram": True,
            "diagram_svg": svg_coins,
            "given": "Coin tossed 3 times. Sample space S = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}. Total outcomes n(S) = 2³ = 8. Hanif wins on HHH or TTT.",
            "formula": "P(Hanif loses) = 1 - P(Hanif wins) = (Total - Winning outcomes) / Total.",
            "substitution": "Winning outcomes = {HHH, TTT} ⇒ 2 outcomes. Losing outcomes = 8 - 2 = 6 outcomes. P(loses) = 6 / 8 = 3 / 4.",
            "calculation": "6/8 = 3/4 = 0.75.",
            "finalAnswer": "3/4 (or 0.75)",
            "unit": "probability",
            "solution": "GIVEN:\nA coin is tossed 3 times.\nTotal elementary outcomes, n(S) = 2³ = 8:\nS = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}.\nHanif wins if all tosses give the same result (three heads or three tails).\n\nTO FIND:\nProbability that Hanif will lose the game.\n\nSTEP-BY-STEP CALCULATION:\nStep 1: Identify winning outcomes for Hanif:\nWinning = {HHH, TTT} (2 outcomes).\nP(Hanif wins) = 2 / 8 = 1 / 4.\n\nStep 2: Identify losing outcomes for Hanif:\nHanif loses on any mixed toss:\nLosing outcomes = {HHT, HTH, HTT, THH, THT, TTH} (6 outcomes).\nP(Hanif loses) = 6 / 8 = 3 / 4 = 0.75.\n(Alternatively: 1 - P(wins) = 1 - 1/4 = 3/4).\n\n[ROUGH_WORK]\n8 outcomes. 2 win, 6 lose. 6/8 = 3/4 = 0.75.\nBoxed Answer: [ 3/4 (or 0.75) ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 209] Exercise 14.1 Q24: A die is thrown twice. What is the probability that (i) 5 will not come up either time? (ii) 5 will come up at least once? (Hint: Throwing a die twice and throwing two dice simultaneously are treated as the same experiment).",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 209,
            "image_search_query": "die thrown twice 5 appears at least once probability",
            "has_diagram": True,
            "diagram_svg": svg_dice,
            "given": "A die thrown twice. Total outcomes n(S) = 6 × 6 = 36.",
            "formula": "Outcomes where 5 comes up at least once: (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (1,5), (2,5), (3,5), (4,5), (6,5) ⇒ 11 outcomes.\nP(5 does not come up either time) = (36 - 11) / 36 = 25 / 36.",
            "substitution": "(i) 5 will not come up either time = (5 choices for first throw) × (5 choices for second throw) = 25 outcomes. P = 25 / 36.\n(ii) 5 will come up at least once = 1 - 25/36 = 11 / 36.",
            "calculation": "(i) 25/36. (ii) 11/36.",
            "finalAnswer": "(i) 25/36, (ii) 11/36",
            "unit": "probability",
            "solution": "GIVEN:\nA die is thrown twice.\nTotal possible outcomes, n(S) = 6 × 6 = 36.\n\nTO FIND:\n(i) Probability that 5 will not come up either time.\n(ii) Probability that 5 will come up at least once.\n\nSTEP-BY-STEP CALCULATION:\nPart (i): 5 will not come up either time:\nFor each throw, there are 5 numbers other than 5: {1, 2, 3, 4, 6}.\nNumber of pairs with no 5s = 5 × 5 = 25.\nP(5 will not come up either time) = 25 / 36.\n\nPart (ii): 5 will come up at least once:\nThis is the complement of the event '5 will not come up either time':\nP(5 comes up at least once) = 1 - P(5 will not come up either time)\n= 1 - (25 / 36) = 11 / 36.\n\nVerification by counting favourable pairs directly:\nPairs with 5 on first die: (5,1), (5,2), (5,3), (5,4), (5,5), (5,6) [6 pairs]\nPairs with 5 on second die: (1,5), (2,5), (3,5), (4,5), (6,5) [5 pairs, (5,5) already counted]\nTotal favourable pairs = 6 + 5 = 11.\nP = 11 / 36.\n\n[ROUGH_WORK]\n25/36 and 11/36. Sum = 36/36 = 1.\nBoxed Answer: [ (i) 25/36, (ii) 11/36 ].",
            "concept_questions": []
        },
        {
            "problem": "[NCERT Class 10 Ch 14 | Section 14.1 | Page 209] Exercise 14.1 Q25: Which of the following arguments are correct and which are not correct? Give reasons for your answer.\n(i) If two coins are tossed simultaneously there are three possible outcomes—two heads, two tails or one of each. Therefore, for each of these outcomes, the probability is 1/3.\n(ii) If a die is thrown, there are two possible outcomes—an odd number or an even number. Therefore, the probability of getting an odd number is 1/2.",
            "section": "14.1 Probability — A Theoretical Approach",
            "page_number": 209,
            "image_search_query": "probability arguments validity two coins die odd even",
            "has_diagram": False,
            "diagram_svg": None,
            "given": "Two probabilistic arguments regarding coin tossing and die rolling.",
            "formula": "Arguments are correct only if the classified outcomes are mutually exclusive and equally likely.",
            "substitution": "(i) Incorrect: 'one of each' has 2 elementary outcomes (HT, TH), so P(one of each) = 2/4 = 1/2, not 1/3.\n(ii) Correct: Odd numbers = {1, 3, 5} (3 outcomes), Even numbers = {2, 4, 6} (3 outcomes). P(odd) = 3/6 = 1/2.",
            "calculation": "(i) Incorrect. (ii) Correct.",
            "finalAnswer": "(i) Incorrect (outcomes are not equally likely: P(one of each) = 1/2); (ii) Correct (odd and even are equally likely: P = 3/6 = 1/2)",
            "unit": "conceptual reasoning",
            "solution": "GIVEN:\nTwo probabilistic assertions.\n\nTO EVALUATE:\nDetermine whether each argument is correct or incorrect with mathematical reasons.\n\nSTEP-BY-STEP EVALUATION:\nStatement (i): INCORRECT.\nReason: When two coins are tossed simultaneously, the true elementary sample space has 4 equally likely outcomes:\nS = {(H, H), (H, T), (T, H), (T, T)}.\n- 'Two heads' = {(H, H)} ⇒ Probability = 1/4.\n- 'Two tails' = {(T, T)} ⇒ Probability = 1/4.\n- 'One of each' = {(H, T), (T, H)} ⇒ Probability = 2/4 = 1/2.\nSince 'one of each' occurs twice as frequently as two heads or two tails, these three outcomes are NOT equally likely. Therefore, the probability is not 1/3.\n\nStatement (ii): CORRECT.\nReason: When a die is thrown, the sample space is {1, 2, 3, 4, 5, 6} with 6 equally likely outcomes.\n- Odd numbers = {1, 3, 5} (3 outcomes) ⇒ P(Odd) = 3/6 = 1/2.\n- Even numbers = {2, 4, 6} (3 outcomes) ⇒ P(Even) = 3/6 = 1/2.\nSince the two categories have identical frequencies (3 each), they are equally likely, and the probability of getting an odd number is indeed 1/2.\n\n[ROUGH_WORK]\n(i) 1/4, 1/2, 1/4 ≠ 1/3 each. (ii) 3/6 = 1/2 = correct.\nBoxed Answer: [ (i) Incorrect, (ii) Correct ].",
            "concept_questions": []
        }
    ]

    # Load existing module metadata
    with open("scripts/maths_class10_modules/ch14_probability.json", "r", encoding="utf-8") as f:
        modules = json.load(f)

    modules[0]["worked_examples"] = m1_worked_examples
    modules[1]["worked_examples"] = m2_worked_examples
    modules[2]["worked_examples"] = m3_worked_examples
    modules[3]["worked_examples"] = m4_worked_examples
    modules[4]["worked_examples"] = m5_worked_examples

    return modules

if __name__ == "__main__":
    mods = get_ch14_complete_modules()
    out_file = "scripts/maths_class10_modules/ch14_probability.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(mods, f, indent=2, ensure_ascii=False)
    
    total_we = sum(len(m["worked_examples"]) for m in mods)
    print(f"Ch 14 complete: {len(mods)} modules, {total_we} worked examples saved to {out_file}.")
