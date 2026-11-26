def refund_system():
    print("AIRLINE REFUND EXPERT SYSTEM")
    fare = input("Enter fare class (Business/Economy): ").lower()
    hours = int(input("Hours before departure: "))
    reason = input("Cancellation reason: ").lower()
    price = float(input("Ticket price: "))
    tier = input("Frequent flyer tier (Gold/Silver/Normal): ").lower()
    claims = int(input("Past refund claims: "))
    facts = {
        "fare": fare,
        "hours": hours,
        "reason": reason,
        "price": price,
        "tier": tier,
        "claims": claims
    }
    rules = [
        (100, "Fraud detected", lambda f: f["reason"] == "fraud", "REJECT"),
        (95, "Duplicate refund claim", lambda f: f["reason"] == "duplicate", "REJECT"),
        (90, "Departure already passed", lambda f: f["hours"] < 0, "REJECT"),
        (85, "Medical emergency", lambda f: f["reason"] == "medical", "APPROVE"),
        (84, "Flight cancelled by airline", lambda f: f["reason"] == "airline cancelled", "APPROVE"),
        (80, "Refundable fare", lambda f: f["fare"] == "business", "APPROVE"),
        (75, "Business class cancellation before departure", lambda f: f["fare"] == "business" and f["hours"] > 24, "APPROVE"),
        (70, "Gold member benefit", lambda f: f["tier"] == "gold" and f["hours"] > 48, "APPROVE"),
        (65, "Early cancellation", lambda f: f["hours"] > 168, "APPROVE"),
        (60, "Non-refundable economy ticket", lambda f: f["fare"] == "economy", "REJECT"),
        (55, "Late economy cancellation", lambda f: f["fare"] == "economy" and f["hours"] < 24, "REJECT"),
        (50, "Multiple previous claims", lambda f: f["claims"] >= 3, "ESCALATE"),
    ]
    fired = []
    for priority, name, condition, decision in rules:
        if condition(facts):
            fired.append((priority, name, decision))
    if fired:
        fired.sort(key=lambda x: x[0], reverse=True)
        print("\nRules Fired:")
        for rule in fired:
            print(rule[1], "->", rule[2])
        print("\nFinal Decision:", fired[0][2])
        print("Reason:", fired[0][1])
    else:
        print("\nFinal Decision: ESCALATE")
        print("Reason: Manual verification required.")
refund_system()
