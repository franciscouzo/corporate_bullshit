import random

def make_eventual_plural(s, plural):
    if len(s) < 1 or not plural:
        return s
    elif s == "matrix":
        return "matrices"
    elif s == "analysis":
        return "analyses"
    else:
        if s[-1] in "sxzh":
            return s + "es"
        elif s[-1] == "y":
            return s[:-1] + "ies"
        else:
            return s + "s"

def build_plural_verb(verb, plural):
    last = len(verb.rstrip()) - 1
    if plural:
        return verb
    else:
        if verb[last] in "osz":
            return verb[:last + 1] + "es" + verb[last + 1:]
        elif verb[last] == "h":
            if verb[last - 1] in "cs":
                return verb[:last + 1] + "es" + verb[last + 1:]
            else:
                return verb[:last + 1] + "s" + verb[last + 1:]
        elif verb[last] == "y":
            if verb[last - 1] in "aeiou":
                return verb[:last + 1] + "s" + verb[last + 1:]
            else:
                return verb[:last] + "ies" + verb[last + 1:]
        else:
            return verb[:last + 1] + "s" + verb[last + 1:]

def add_indefinite_article(s, plural):
    if plural:
        return s
    else:
        if s[0] in "aeiou":
            return "an " + s
        else:
            return "a " + s

def weighted_choice(choices):
    total = sum(w for c, w in choices.iteritems())
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices.iteritems():
        if upto + w > r:
            return c
        upto += w

def boss():
    managing = weighted_choice({"Managing ": 1, "Acting ": 1, "": 6})
    vice = weighted_choice({"Vice ": 1, "": 3})
    co = weighted_choice({"Co-": 1, "": 3})
    title = random.choice((
        vice + "Director", "Chief", co + "Head", vice + "President"
    ))
    age = weighted_choice({"Senior ": 1, "": 3})
    exec_ = weighted_choice({"Excutive ": 1, "": 5})
    groupal = weighted_choice({"Group ": 1, "Global": 1, "": 18})
    department = random.choice((
        "Human Resources", "Controlling", "Internal Audit", "Legal",
        "Operations", "Management Office", "Customer Relations",
        "Client Leadership", "Client Relationship", "Business Planning",
        "Business Operations", "IT Strategy", "IT Operations"
    ))
    department_or_top_role = weighted_choice({department: 13, "Visionary": 1})
    boss = weighted_choice({
        managing + age + exec_ + title + " of " + department: 1,
        groupal + "Chief " + department_or_top_role + " Officer": 3
    })
    return boss

def person(plural):
    if not plural:
        r = random.randint(1, 17)
        if r <= 12:
            return random.choice((
                "steering committee", "group", "project manager",
                thing_atom(random.choice((True, False))) + " champion",
                "community", "sales manager", "enabler", "powerful champion",
                "thought leader", "gatekeeper", "resource",
                "senior support staff"
            ))
        else:
            return boss()
    else:
        return random.choice((
            "key people", "human resources", "customers", "clients",
            "resources", "team players", "enablers", "stakeholders",
            "standard-setters", "partners", "business leaders"
        ))

def matrix_or_so():
    return weighted_choice({
        "organization": 2, "silo": 3, "matrix": 3, "cube": 1, "sphere": 1
    })

def thing_adjective():
    return random.choice((
        "efficient", "strategic", "constructive", "proactive", "strong",
        "key", "global", "corporate", "cost-effective", "focused", "top-line",
        "credible", "agile", "holistic", "new", "adaptive", "optimal",
        "unique", "core", "compliant", "goal-oriented", "non-linear",
        "problem-solving", "prioritizing", "cultural", "future-oriented",
        "potential", "versatile", "leading", "dynamic", "progressive",
        "non-deterministic", "informed", "leveraged", "challenging",
        "intelligent", "controlled", "educated", "non-standard", "underlying",
        "centralized", "decentralized", "reliable", "consistent", "competent",
        "prospective", "collateral", "functional", "tolerably expensive",
        "organic", "forward-looking", "next-level", "executive", "seamless",
        "spectral", "balanced", "effective", "integrated", "systematized",
        "parallel", "responsive", "synchronized", "compatible",
        "carefully thought-out", "cascading", "high-level", "siloed",
        "operational", "future-ready", "flexible", "movable", "right",
        "productive", "evolutionary", "overarching", "documented", "awesome",
        "coordinated", "aligned", "enhanced", "replacement",
        "industry-standard", "accepted", "agreed-upon", "target",
        "customer-centric", "wide-spectrum", "well-communicated",
        "cutting-edge", "best-in-class", "state-of-the-art", "verifiable",
        "solid", "inspiring", "growing", "market-altering", "vertical",
        "emerging", "differentiating", "integrative", "cross-functional",
        "measurable", "well-planned", "accessible", "actionable",
        "accurate", "insightful", "relevant", "long-term", "top", "tactical",
        "best-of-breed", "robust", "targeted", "personalized", "interactive",
        "streamlined", "transparent", "traceable", "far-reaching", "powerful",
        "improved", "executive-level", "goal-based", "top-level",
        "cooperative", "value-adding", "streamlining", "time-honored",
        "idiosyncratic", "sustainable", "in-depth", "immersive",
        "cross-industry", "time-phased", "day-to-day", "present-day",
        "medium-to-long-term", "profit-maximizing", "generic", "granular",
        "market-driven", "value-driven", "well-defined", "outward-looking",
        "scalable", "strategy-focused", "promising", "collaborative",
        "scenario-based", "principle-based", "vision-setting",
        "client-oriented", "long-established", "established",
        "organizational", "visionary", "trusted", "full-scale", "firm-wide",
        "fast-growth", "performance-based", "high-performing", "top-down",
        "cross-enterprise", "outsourced", "situational", "bottom-up",
        "multidisciplinary", "one-to-one", "goal-directed",
        "intra-organisational", "high-performing", "multi-source",
        "360-degree", "motivational", "differentiated", "solutions-based",
        "compelling", "structural", "go-to-market", "on-message", "adequate",
        "value-enhancing", "mission-critical", "business enabling",
        "transitional", "future", "game-changing", "enterprise-wide",
        "rock-solid", "bullet-proof", "superior", "genuine", "alert",
        "nimble", "phased", "selective", "macroscopic", "low-risk high-yield",
        "interconnected", "high-margin"
    ))

def timeless_event():
    return random.choice((
        "kick-off", "roll-out", "client event", "quarter results"
    ))

def growth():
    superlative = random.choice((
        "organic", "double-digit", "upper single-digit", "breakout",
        "unprecedented", "unparallelled", "proven", "measured"
    ))
    improvement = random.choice((
        "growth", "improvement", "throughput increase", "efficiency gain",
        "yield enhancement"
    ))
    return superlative + " " + improvement;

def thing_atom(plural):
    r = random.randint(1, 170)
    if r == 1:
        inner = matrix_or_so()
    else:
        inner = random.choice((
            "mission", "vision", "guideline", "roadmap", "timeline",
            "win-win solution", "baseline starting point", "sign-off",
            "escalation", "system", "Management Information System",
            "Quality Management System", "planning", "target", "calibration",
            "Control Information System", "process", "talent", "execution",
            "leadership", "performance", "solution provider", "value",
            "value creation", "feedback", "document","bottom line", "momentum",
            "opportunity", "credibility", "issue", "core meeting", "platform",
            "niche", "content", "communication", "goal", "skill", "alternative",
            "culture", "requirement", "potential", "challenge", "empowerment",
            "benchmarking", "framework", "benchmark", "implication",
            "integration", "enabler", "control", "trend", "business case",
            "architecture", "action plan", "project", "review cycle",
            "trigger event", "strategy formulation", "decision",
            "enhanced data capture", "energy", "plan", "initiative", "priority",
            "synergy", "incentive", "dialogue", "concept", "time-phase",
            "projection", "blended approach", "low hanging fruit",
            "forward planning", "pre-plan", "pipeline", "bandwidth", "workshop",
            "paradigm", "paradigm shift", "strategic staircase", "cornerstone",
            "executive talent", "evolution", "workflow", "message",
            "risk/return profile", "efficient frontier", "pillar",
            "internal client", "consistency", "on-boarding process",
            "dotted line", "action item", "cost efficiency", "channel",
            "convergence", "infrastructure", "metric", "technology",
            "relationship", "partnership", "supply-chain", "portal", "solution",
            "business line", "white paper", "scalability", "innovation",
            "Strategic Management System", "Balanced Scorecard", "differentiator",
            "case study", "idiosyncrasy", "benefit", "say/do ratio",
            "segmentation", "image", "realignment", "business model",
            "business philosophy", "branding", "methodology", "profile",
            "measure", "measurement", "philosophy", "branding strategy",
            "efficiency", "industry", "commitment", "perspective",
            "risk appetite", "best practice", "brand identity",
            "customer centricity", "shareholder value", "attitude", "mindset",
            "flexibility", "granularity", "engagement", "pyramid", "market",
            "diversity", "interdependency", "scaling", "asset", "flow charting",
            "value proposition", "performance culture", "change", "reward",
            "learning", "next step", "delivery framework", "structure",
            "support structure", "standardization", "objective", "footprint",
            "transformation process", "policy", "sales target", "ecosystem",
            "market practice", "atmosphere", "operating strategy",
            "core competency"
        ))

    if not plural:
        r = random.randint(1, 200)
        if r == 1:
            return timeless_event()
        elif r <= 78:
            return random.choice((
                "team building", "focus", "strategy",
                "planning granularity", "core business", "implementation",
                "intelligence", "governance", "ROE", "EBITDA",
                "enterprise content management", "excellence", "trust",
                "respect", "openness", "transparency", "Quality Research",
                "decision making", "risk management",
                "enterprise risk management", "leverage", "diversification",
                "successful execution", "effective execution", "selectivity",
                "optionality", "expertise", "awareness", "broader thinking",
                "client focus", "thought leadership", "quest for quality",
                "360-degree thinking", "drill-down", "impetus", "fairness",
                "intellect", "emotional impact", "emotional intelligence",
                "adaptability", "stress management", "self-awareness",
                "strategic thinking", "cross fertilization", "effectiveness",
                "customer experience", "centerpiece", "SWOT analysis",
                "responsibility", "accountability", "ROI", "line of business",
                "serviceability", "responsiveness", "simplicity",
                "portfolio shaping", "knowledge sharing", "continuity",
                "visual thinking", "interoperability", "compliance",
                "teamwork", "self-efficacy", "decision-making",
                "line-of-sight", "scoping", "line-up", "predictability",
                "recognition", "investor confidence", "competitive advantage",
                "uniformity", "competitiveness", "big picture",
                "resourcefulness", "quality", "upside focus"
            ))
        else:
            return inner
    else:
        r = random.randint(1, 200)
        if r <= 12:
            return random.choice((
                "key target markets", "style guidelines",
                "key performance indicators", "market conditions",
                "market forces", "market opportunities", "tactics",
                "organizing principles", "interpersonal skills",
                "roles and responsibilities", "cost savings",
                "lessons learned"
            ))
        else:
            return make_eventual_plural(inner, True)

def thing(plural):
    r = random.randint(1, 110)
    if r <= 10:
        return thing_adjective() + ", " + thing_adjective() + " " + thing_atom(plural)
    elif r <= 15:
        return thing_adjective() + " and " + thing_adjective() + " " + thing_atom(plural)
    elif r <= 71:
        return thing_adjective() + " " + thing_atom(plural)
    elif r <= 73:
        return thing_adjective() + " and/or " + thing_adjective() + " " + thing_atom(plural)
    elif r <= 75:
        return growth()
    elif r <= 80:
        return thing_adjective() + ", " + thing_adjective() + " and " + thing_adjective() + " " + thing_atom(plural)
    elif r <= 85:
        return thing_adjective() + ", " + thing_adjective() + ", " + thing_adjective() + " and " + thing_adjective() + " " + thing_atom(plural)
    else:
        return thing_atom(plural)

def bad_things():
    return random.choice((
        "issues", "intricacies", "organizational diseconomies", "black swans",
        "gaps", "inefficiencies", "overlaps", "known unknowns",
        "unknown unknowns", "soft cycle issues", "obstacles", "surprises",
        "weaknesses", "threats", "barriers to success", "barriers",
        "shortcomings", "problems", "uncertainties"
    ))

def eventual_adverb():
    r = random.randint(1, 4)
    if r == 1:
        return random.choice((
            "interactively", "credibly", "quickly", "proactively", "200%",
            "24/7", "globally", "culturally", "technically", "strategically",
            "swiftly", "cautiously", "expediently", "organically",
            "carefully", "significantly", "conservatively","adequately",
            "genuinely"
        )) + " "
    else:
        return ""

def add_random_article(s, plural):
    r = random.randint(1, 15)
    if r <= 2:
        return "the " + s
    elif r <= 6:
        return "our " + s
    else:
        return add_indefinite_article(s, plural)

def eventual_postfixed_adverb():
    plural = random.choice((True, False))
    r = random.randint(1, 140)
    if r <= 15:
        return random.choice((
            " going forward", " within the industry", " across the board",
            " in this space", " from the get-go", " at the end of the day",
            " throughout the organization", " as part of the plan",
            " by thinking outside of the box", " ahead of schedule",
            ", relative to our peers", " on a transitional basis",
            " by expanding boundaries", " by nurturing talent",
            ", as a Tier 1 company"
        ))
    elif r == 16:
        return " using " + add_random_article(thing(plural), plural)
    elif r == 17:
        return " by leveraging " + add_random_article(thing(plural), plural)
    elif r == 18:
        return " taking advantage of " + add_random_article(thing(plural), plural)
    elif r == 19:
        return " within the " + matrix_or_so()
    elif r == 20:
        return " across the " + make_eventual_plural(matrix_or_so(), plural)
    elif r == 21:
        return " up-front"
    elif r == 22:
        return " resulting in " + growth()
    elif r == 23:
        return " reaped from our " + growth()
    elif r == 24:
        return " as a consequence of " + growth()
    elif r == 25:
        return (" because " + add_random_article(thing(plural), plural) + " " +
                      build_plural_verb("produce", plural) + " " + growth())
    else:
        return ""

def person_verb_having_thing_complement(plural):
    inner = random.choice((
        "manage", "target", "streamline", "improve", "optimize", "achieve",
        "secure", "address", "boost", "deploy", "innovate", "right-scale",
        "formulate", "transition", "leverage", "focus on", "synergize",
        "generate", "analyse", "integrate", "empower", "benchmark", "learn",
        "adapt", "enable", "strategize", "prioritize", "pre-prepare",
        "deliver", "champion", "embrace", "enhance", "engineer", "envision",
        "incentivize", "maximize", "visualize", "whiteboard",
        "institutionalize", "promote", "overdeliver", "right-size",
        "rebalance", "re-imagine", "influence", "facilitate", "drive",
        "structure", "standardize", "accelerate", "deepen", "strengthen",
        "broaden", "enforce", "establish", "foster", "build", "differentiate",
        "take a bite out of", "table", "flesh out", "reach out"
    ))
    return build_plural_verb(inner, plural)

def person_verb_having_bad_thing_complement(plural):
    inner = random.choice(("address", "identify", "avoid", "mitigate"))
    return build_plural_verb(inner, plural)

def thing_verb_having_thing_complement(plural):
    inner = random.choice((
        "streamline", "interact with", "boost", "generate", "impact",
        "enhance", "leverage", "synergize", "generate", "empower", "enable",
        "prioritize", "transfer", "drive", "result in", "promote",
        "influence", "facilitate", "aggregate", "architect", "cultivate",
        "engage", "structure", "standardize", "accelerate", "deepen",
        "strengthen", "enforce", "foster"
    ))
    return build_plural_verb(inner, plural)

def thing_verb_having_person_complement(plural):
    inner = random.choice((
        "motivate", "target", "enable", "drive", "synergize", "empower",
        "prioritize", "incentivise", "inspire", "transfer", "promote",
        "influence", "strengthen"
    ))
    return build_plural_verb(inner, plural)

def person_verb_and_complement(plural):
    inner = random.choice((
        "streamline the process", "address the overarching issues",
        "benchmark the portfolio", "manage the cycle",
        "figure out where we come from, where we are going to",
        "maximize the value", "execute the strategy", "think out of the box",
        "think differently", "manage the balance", "loop back", "conversate",
        "go forward together", "achieve efficiencies", "deliver",
        "stay in the mix", "stay in the zone", "evolve",
        "exceed expectations", "develop the plan",
        "develop the blue print for execution", "grow and diversify",
        "fuel changes", "nurture talent", "turn every stone",
        "challenge established ideas", "manage the portfolio",
        "align resources", "drive the business forward", "make things happen",
        "stay ahead", "outperform peers", "surge ahead",
        "manage the downside", "stay in the wings", "come to a landing",
        "shoot it over", "move the needle", "connect the dots",
        "connect the dots to the end game", "reset the benchmark",
        "take it offline", "peel the onion", "drill down"
    ))
    return build_plural_verb(inner, plural)

def thing_verb_and_ending(plural):
    compl_sp = random.choice((True, False))

    r = random.randint(1, 101)
    if r <= 55:
        return (thing_verb_having_thing_complement(plural) + " " +
            add_random_article(thing(compl_sp), compl_sp))
    elif r <= 100:
        return (thing_verb_having_person_complement(plural) + " the " +
            person(compl_sp))
    else:
        return build_plural_verb("add", plural) + " value"

def person_verb_and_ending(plural):
    compl_sp = random.choice((True, False))
    
    r = random.randint(1, 95)
    if r <= 10:
        return person_verb_and_complement(plural)
    elif r <= 15:
        return (person_verb_having_bad_thing_complement(plural) + " " +
            add_random_article(bad_things(), plural))
    else:
        return (person_verb_having_thing_complement(plural) + " " +
            add_random_article(thing(compl_sp), compl_sp))

def faukon():
    r = random.randint(1, 6)
    if r <= 5:
        return random.choice((
            "we need to", "we've got to", "the reporting unit should",
            "controlling should",
            "pursuing this route will enable us to"
        ))
    else:
        return "we must activate the " + matrix_or_so() + " to"

def proposition():
    plural = random.choice((True, False))
    r = random.randint(1, 100)
    if r <= 5:
        return (faukon() + " " + eventual_adverb() + person_verb_and_ending(True) +
            eventual_postfixed_adverb())
    elif r <= 50:
        return ("the " + person(plural) + " " + eventual_adverb() +
            person_verb_and_ending(plural) + eventual_postfixed_adverb())
    else:
        return (add_random_article(thing(plural), plural) + " " + eventual_adverb() +
            thing_verb_and_ending(plural) + eventual_postfixed_adverb())

def articulated_propositions():
    r = random.randint(1, 28)
    if r <= 17:
        return proposition()
    elif r == 18:
        return proposition() + "; this is why " + proposition()
    elif r == 19:
        return proposition() + "; nevertheless " + proposition()
    elif r == 20:
        return proposition() + ", whereas " + proposition()
    elif r == 21:
        return "our gut-feeling is that " + proposition()
    elif r <= 25:
        return proposition() + ", while " + proposition()
    elif r == 26:
        return proposition() + ". In the same time, " + proposition()
    elif r == 27:
        return proposition() + ". As a result, " + proposition()
    else:
        return proposition() + ", whilst " + proposition()

def sentence():
    return articulated_propositions().capitalize() + "."

def sentences():
    ret = []
    for i in xrange(max(3, int(random.normalvariate(30, 10)))):
        ret.append(sentence())
    return " ".join(ret)

def sentence_guaranteed_amount(count):
    return " ".join(sentence() for i in xrange(count))

def workshop():
    return sentence_guaranteed_amount(500, dialog_mark)

def short_workshop():
    return sentence_guaranteed_amount(5, dialog_mark)

def financial_report():
    return sentences("")