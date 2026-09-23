TASK = {
    "name": "format_number",
    "description": "Írj egy Python függvényt `format_number(n)` néven, ami egy számot (int vagy float) formázott stringgé alakít a következő PONTOS szabályok szerint: 1) Az ezres helyiértékeket aposztróf (') karakter választja el, NEM vessző és NEM szóköz (pl. 1000 -> \"1'000.00\"). 2) Mindig pontosan 2 tizedesjegyet kell mutatni, akkor is, ha a szám egész (pl. 1000 -> \"1'000.00\", nem \"1'000\" vagy \"1'000.0\"). 3) Negatív számoknál a mínuszjel a string legelején álljon, a helyes ezres csoportosítás mellett (pl. -1234.5 -> \"-1'234.50\", nem \"1'234.50-\" vagy hibás csoportosítás). 4) Nagy számoknál minden háromjegyű csoportot külön aposztróffal kell elválasztani, jobbról balra haladva (pl. 1000000 -> \"1'000'000.00\").",
    "tests": [
        {"input": 1000, "expected": "1'000.00"},
        {"input": -1234.5, "expected": "-1'234.50"},
        {"input": 0, "expected": "0.00"},
        {"input": 999, "expected": "999.00"},
        {"input": 1234567.891, "expected": "1'234'567.89"},
        {"input": 100000, "expected": "100'000.00"},
        {"input": -999, "expected": "-999.00"},
        {"input": 1000000000, "expected": "1'000'000'000.00"},
    ]
}
