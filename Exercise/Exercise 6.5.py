text = "X-DSPAM-Confidence:    0.8475";

index1 = text.find("0")
index2 = text.find("5")

print(float(text[index1:int(index2)+1]))
