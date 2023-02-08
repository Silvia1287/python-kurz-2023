import json
with open ("body.json", encoding = "utf-8") as subor:
    slovnik = json.load(subor)


prospech = {

}

for meno in slovnik:
    if slovnik[meno]> 60:
        prospech[meno] = "pass"
    else:
        prospech[meno] = "fail"

print(prospech)
   
with open("slovnik.json", "w") as subor:
    json.dump(prospech, subor, ensure_ascii=False)