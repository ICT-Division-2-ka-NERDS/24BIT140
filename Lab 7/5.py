prices={"rice":40,"dal":80,"vegetables":30,"milk":45,"tea":150}
quantities={"rice":5,"dal":2,"vegetables":3,"milk":10,"tea":1}

bill=0
for i in prices:
    bill+=(prices[i]*quantities[i])

print("Final bill:",bill)