import random


def make_eventual_plural(word, plural):
    if len(word) < 3 or not plural:
        return word

    try:
        abbr = word.index(" (")
        return make_eventual_plural(word[:abbr], plural) + word[abbr:]
    except ValueError:
        pass

    if word == "matrix":
        return "matrices"
    elif word == "analysis":
        return "analyses"
    elif word[-2:] == "gh":
        return word + "s"
    elif word[-1] in "sxzh":
        return word + "es"
    elif word[-1] == "y" and word[-2].lower() not in "aeiou":
        return word[:-1] + "ies"

    return word + "s"


def build_plural_verb(verb, plural):
    last = len(verb.rstrip()) - 1
    if plural:
        return verb

    if verb[last] in "osz":
        return verb[:last + 1] + "es" + verb[last + 1:]
    elif verb[last] == "h":
        if verb[last - 1] in "cs":
            return verb[:last + 1] + "es" + verb[last + 1:]

        return verb[:last + 1] + "s" + verb[last + 1:]
    elif verb[last] == "y":
        if verb[last - 1].lower() in "aeiou":
            return verb[:last + 1] + "s" + verb[last + 1:]

        return verb[:last] + "ies" + verb[last + 1:]

    return verb[:last + 1] + "s" + verb[last + 1:]


def add_indefinite_article(word, plural):
    if plural:
        return word

    if word[0].lower() in "aeiou":
        return "an " + word

    return "a " + word


def silly_abbreviation_generator_sas(s):
    return "".join(word[0] for word in s.split(" "))


def abbreviate(s, probability):
    if random.random() < probability:
        return s + " (" + silly_abbreviation_generator_sas(s) + ")"

    return s


def weighted_choice(choices):
    total = sum(choices.values())
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices.items():
        if upto + w > r:
            return c
        upto += w


def boss():
    department = random.choice((
        "Human Resources", "Controlling", "Internal Audit", "Legal",
        "Operations", "Management Office", "Customer Relations",
        "Client Leadership", "Client Relationship", "Business Planning",
        "Business Operations", "IT Strategy", "IT Operations", "Marketing",
        "Strategic Planning", "Facilities Management", "Innovation",
        "Identity", "Branding", "Diversity and Inclusion", "Media Relations",
        "Value Added Services", "Technology", "Campaigning",
        "Digital Marketing", "Digital Transformation Office", "Communications",
        "Architecture", "Data & Analytics", "Compliance",
        "Research & Development", "Networking Enhancement",
        "Innovative Strategies", "Global Innovation Insight",
        "Transition Transformation", "Change Management", "Global Strategy",
        "Creativity and Innovation", "Information Security"
    ))
    department_or_top_role = weighted_choice({
        department: 39, "Visionary": 1, "Digital": 1, "Technical": 1,
        "Manifesto": 1, "Operating": 1, "Product": 1, "Scheme": 1,
        "Growth": 1, "Brand": 1, "Sales": 1, "Networking": 1, "Content": 1,
        "Holacracy": 1
    })

    if random.randint(1, 4) == 1:
        managing = weighted_choice({
            "Managing ": 1, "Acting ": 1, "General": 1, "": 5})
        vice = weighted_choice({"Vice ": 10, "Corporate Vice ": 1, "": 29})
        co = weighted_choice({"Co-": 1, "": 4})
        title = random.choice((
            vice + co + "Director", co + "Chief", co + "Head",
            vice + co + "President", "Supervisor", co + "Manager"
        ))
        age = weighted_choice({"Senior ": 1, "": 3})
        exec_ = weighted_choice({"Excutive ": 1, "Principal ": 1, "": 10})
        return managing + age + exec_ + title + " of " + department

    groupal = weighted_choice({"Group ": 1, "Global ": 1, "": 18})
    officer_or_catalyst = weighted_choice({
        "Catalyst": 1, "Futurist": 1, "Strategist": 1, "Technologist": 1,
        "Officer": 16
    })
    return groupal + abbreviate("Chief " + department_or_top_role + " " +
                                officer_or_catalyst, 0.6)


def person(plural):
    if not plural:
        r = random.randint(1, 45)
        if r == 1:
            return thing_atom(random.choice((True, False))) + " champion"
        elif r <= 31:
            return random.choice((
                "steering committee", "group", "project manager", "community",
                "sales manager", "enabler", "powerful champion",
                "thought leader", "gatekeeper", "resource",
                "senior support staff", "brand manager", "category manager",
                "account executive", "project leader", "product manager",
                "naming committee", "executive committee",
                "white-collar workforce", "innovator", "game changer",
                "visionary", "market thinker", "network", "initiator",
                "change agent", "rockstar", "facilitator", "disruptor",
                "challenger"
            ))

        return boss()

    return random.choice((
        "key people", "human resources", "customers", "clients", "resources",
        "team players", "enablers", "stakeholders", "standard-setters",
        "partners", "business leaders", "thinkers/planners",
        "white-collar workers", "board-level executives",
        "key representatives", "innovators", "policy makers", "pioneers",
        "game changers", "market thinkers", "thought leaders", "mediators",
        "facilitators", "attackers", "initiators", "decision makers",
        "Growth Hackers", "Digital Marketers", "Creative Technologists",
        "Products Managers", "Products Owners", "disruptors", "challengers"
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
        "parallel", "responsive", "synchronized", "carefully-designed",
        "carefully thought-out", "cascading", "high-level", "siloed",
        "operational", "future-ready", "flexible", "movable", "right",
        "productive", "evolutionary", "overarching", "documented", "awesome",
        "coordinated", "aligned", "enhanced", "control-based",
        "industry-standard", "accepted", "agreed-upon", "target",
        "customer-centric", "wide-spectrum", "well-communicated",
        "cutting-edge", "state-of-the-art", "verifiable", "six-sigma", "solid",
        "inspiring", "growing", "market-altering", "vertical", "emerging",
        "differentiating", "integrative", "cross-functional", "measurable",
        "well-planned", "accessible", "actionable", "accurate", "insightful",
        "relevant", "long-term", "longer-term", "tactical", "best-of-breed",
        "robust", "targeted", "personalized", "interactive", "streamlined",
        "transparent", "traceable", "far-reaching", "powerful", "improved",
        "executive-level", "goal-based", "top-level", "cooperative",
        "value-adding", "streamlining", "time-honored", "idiosyncratic",
        "sustainable", "in-depth", "immersive", "cross-industry",
        "time-phased", "day-to-day", "present-day", "modern-day",
        "profit-maximizing", "generic", "granular", "values-based",
        "value-driven", "well-defined", "outward-looking", "scalable",
        "strategy-focused", "promising", "collaborative", "scenario-based",
        "principle-based", "vision-setting", "client-oriented",
        "long-established", "established", "organizational", "visionary",
        "trusted", "full-scale", "firm-wide", "fast-growth",
        "performance-based", "data-inspired", "high-performance",
        "cross-enterprise", "outsourced", "situational", "bottom-up",
        "multidisciplinary", "one-to-one", "goal-directed",
        "intra-organisational", "high-performing", "multi-source",
        "360-degree", "motivational", "differentiated", "solutions-based",
        "compelling", "structural", "go-to-market", "on-message",
        "productivity-enhancing", "value-enhancing", "mission-critical",
        "business-enabling", "transitional", "future", "game-changing",
        "enterprise-wide", "rock-solid", "bullet-proof", "superior",
        "genuine", "alert", "nimble", "phased", "selective", "macroscopic",
        "low-risk high-yield", "interconnected", "high-margin", "resilient",
        "high-definition", "well-crafted", "fine-grained", "context-aware",
        "multi-tasked", "feedback-based", "analytics-based", "fact-based",
        "usage-based", "multi-channel", "omni-channel", "cross-channel",
        "specific", "heart-of-the-business", "responsible",
        "socially conscious", "results-centric", "business-led",
        "well-positioned", "end-to-end", "high-quality", "siloed", "modular",
        "service-oriented", "competitive", "scale-as-you-grow", "outside-in",
        "hyper-hybrid", "long-running", "large-scale", "wide-ranging",
        "active", "stellar", "dramatic", "aggressive", "innovative",
        "high-powered", "above-average", "result-driven", "innovation-driven",
        "customized", "outstanding", "non-mainstream", "customer-facing",
        "consumer-facing", "unified", "cooperative", "laser-focused",
        "well-implemented", "diversifying", "market-changing",
        "metrics-driven", "pre-integrated", "solution-oriented", "impactful",
        "world-class", "front-end", "leading-edge", "cost-competitive",
        "extensible", "under-the-radar", "high-grade", "structured",
        "trust-based", "intra-company", "inter-company", "profit-oriented",
        "sizeable", "highly satisfactory", "bi-face", "tri-face", "disruptive",
        "technological", "marketplace", "fast-evolving", "open",
        "fully networked", "adoptable", "trustworthy", "science-based",
        "non-manufacturing", "multi-divisional", "controllable",
        "high-priority", "market-driven", "market-driving", "ingenious",
        "business-for-business", "inspirational", "winning", "boundaryless",
        "reality-based", "customer-focused", "preemptive", "location-specific",
        "revealing", "inventory-planning", "ubiquitous", "number-one",
        "results-oriented", "socially enabled", "well-scoped", "insight-based",
        "high-impact", "technology-driven", "knowledge-based",
        "information-age", "technology-centered", "critical", "cognitive",
        "acculturated", "client-centric", "comprehensive", "ground-breaking",
        "long-standing", "accelerating", "forward-thinking", "mind-blowing",
        "jaw-dropping", "transformative", "better-than-planned", "vital",
        "radical", "expanding", "fierce", "single-minded", "mindful",
        "top-down", "hands-on", "one-on-one", "analytic", "top", "elite",
        "dedicated", "curated", "highly-curated", "re-imagined",
        "thought-provoking", "quality-oriented", "task-oriented",
        "teamwork-oriented", "high-growth", "fast-track", "next-generation",
        "new-generation", "best-in-class", "best-of-class", "first-class",
        "top-class", "superior-quality", "synergistic", "micro-macro",
        "organization-wide", "clear-cut", "data-driven", "evidence-based",
        "transformational", "fast-paced", "real-time", "pre-approved",
        "unconventional", "advanced-analytics", "insight-driven",
        "sprint-based", "digitized", "hypothesis-driven", "governance-related",
        "convergent", "leadership-defined", "operations-oriented",
        "long-range", "dimensional", "award-winning", "user-centric",
        "first-to-market", "first-mover", "cross-platform", "on-the-go",
        "all-encompassing", "matrixed", "growth-enabling", "skills-based",
        "bottom-line", "top-shelf", "insourced", "out-of-the-box", "engaging",
        "on- and offline", "goals-based", "enriching", "medium-to-long-term",
        "adequate", "awareness-raising", "compatible", "supportive",
        "inspired", "high-return", "turn-key", "turnkey", "decision-ready",
        "diversified", "demanding", "ambitious", "domain-relevant", "novel",
        "pre-planned", "well-respected", "market-based", "distributor-based",
        "area-wide", "movements-based", "ever-changing", "purpose-driven",
        "resourceful", "real-life", "vibrant", "bright", "pure-play",
        "bespoke", "pivotal", "efficiency-enhancing", "multi-level", "rich",
        "frictionless", "up-to-the-minute", "sourced", "outcome-driven",
        "hyperaware", "high-velocity", "lean", "unmatched", "industry-leading",
        "multi-sided", "tailor-made"
    ))


def timeless_event():
    return random.choice((
        "kick-off", "roll-out", "client event", "quarter results"
    ))


def growth_atom():
    return random.choice((
        "growth", "improvement", "throughput increase", "efficiency gain",
        "yield enhancement", "expansion", "productivity improvement",
        "gain in task efficiency", "shift in value", "increase in margins",
        "cost reduction", "cost effectiveness", "level of change",
        "revenue growth", "profits growth", "growth momentum",
        "increase in sales"
    ))


def growth():
    superlative = random.choice((
        "organic", "double-digit", "upper single-digit", "breakout",
        "unprecedented", "unparallelled", "proven", "measured", "sustained",
        "sustainable", "robust", "solid", "rock-solid", "healthy",
        "incremental", "significant", "recurring", "sizeable", "rapid",
        "breakneck", "profitable", "disciplined", "accelerated", "impressive",
        "superior", "attractive-enough", "continual", "above-potential",
        "better-than-average"
    ))
    return superlative + " " + growth_atom()


def thing_atom(plural):
    def inner():
        r = random.randint(1, 253)
        if r <= 194:
            return matrix_or_so()
        elif r == 195:
            return abbreviate("Management Information System", 0.5)
        elif r == 196:
            return abbreviate("Quality Management System", 0.5)
        elif r == 197:
            return abbreviate("Control Information System", 0.5)
        elif r == 198:
            return abbreviate("Strategic Management System", 0.5)
        elif r == 199:
            return abbreviate("leadership development system", 0.5)

        return random.choice((
            "mission", "vision", "guideline", "roadmap", "timeline",
            "win-win solution", "baseline starting point", "sign-off",
            "escalation", "system", "planning", "target", "calibration",
            "process", "talent", "execution", "leadership", "performance",
            "solution provider", "value", "value creation",
            "value realization", "document", "bottom line", "momentum",
            "opportunity", "credibility", "issue", "core meeting", "platform",
            "niche", "content", "communication", "goal", "value creation goal",
            "alternative", "culture", "requirement", "potential", "challenge",
            "empowerment", "benchmarking", "framework", "benchmark",
            "implication", "integration", "enabler", "control", "trend",
            "business case", "architecture", "action plan", "project",
            "review cycle", "trigger event", "strategy formulation",
            "decision", "enhanced data capture", "energy", "plan",
            "initiative", "priority", "synergy", "incentive", "dialogue",
            "concept", "time-phase", "projection", "blended approach",
            "low hanging fruit", "forward planning", "pre-plan", "pipeline",
            "bandwidth", "workshop", "paradigm", "paradigm shift",
            "strategic staircase", "cornerstone", "executive talent",
            "evolution", "workflow", "message", "risk/return profile",
            "efficient frontier", "pillar", "internal client", "consistency",
            "on-boarding process", "dotted line", "action item",
            "cost efficiency", "channel", "convergence", "infrastructure",
            "metric", "technology", "relationship", "partnership",
            "supply-chain", "portal", "solution", "business line",
            "white paper", "scalability", "innovation", "Balanced Scorecard",
            "key differentiator", "case study", "idiosyncrasy", "benefit",
            "say/do ratio", "segmentation", "image", "realignment",
            "business model", "business philosophy", "branding", "methodology",
            "profile", "measure", "measurement", "philosophy",
            "branding strategy", "efficiency", "industry", "commitment",
            "perspective", "risk appetite", "best practice", "brand identity",
            "customer centricity", "shareholder value", "attitude", "mindset",
            "flexibility", "granularity", "engagement", "pyramid", "market",
            "diversity", "interdependency", "scaling", "asset",
            "flow charting", "value proposition", "performance culture",
            "change", "reward", "learning", "next step", "delivery framework",
            "structure", "support structure", "standardization", "objective",
            "footprint", "transformation process", "policy", "sales target",
            "ecosystem", "market practice", "atmosphere", "operating strategy",
            "core competency", "market practice", "operating strategy",
            "insight", "accomplishment", "correlation", "touchpoint",
            "knowledge transfer", "correlation", "capability", "gamification",
            "smooth transition", "leadership strategy", "collaboration",
            "success factor", "lever", "breakthrough", "open-door policy",
            "recalibration", "wow factor", "onboarding solution",
            "brand pyramid", "dashboard", "branding",
            "local-for-local strategy", "cross-sell message",
            "up-sell message", "divisional structure", "value chain",
            "microsegment", "rollout plan", "architectural approach",
            "brand value", "milestone", "co-innovation", "speedup",
            "validation", "skill", "skillset", "feedback", "learnability",
            "visibility", "agility", "simplification", "digitization",
            "streamlining", "brainstorming space", "crowdsourcing",
            "big-bang approach", "execution message", "criticality",
            "opportunity pipeline", "reorganization", "synergization",
            "socialization", "strategic shift", "growth engine", "tailwind",
            "accelerator", "deliverable", "takeaway", "insourcing",
            "outsourcing", "careful consideration", "conviction", "initiator",
            "operating model", "proof-point", "bounce rate",
            "marketing funnel", "offshoring", "quick-win", "cross-pollination",
            "hybridation", "positioning", "reinvention", "functionality",
            "mindshare", "mobility space", "decision-to-execution cycle",
            "adjustment", "force management program", "launchpad"
        ))

    if not plural:
        r = random.randint(1, 430)
        if r == 1:
            return timeless_event()
        elif r == 2:
            return abbreviate("Quality Research", 0.5)
        elif r <= 177:
            return random.choice((
                "team building", "focus", "strategy",
                "planning granularity", "core business", "implementation",
                "intelligence", "change management", "ROE", "EBITDA",
                "enterprise content management", "excellence", "trust",
                "respect", "openness", "transparency", "decision making",
                "risk management", "enterprise risk management", "leverage",
                "diversification", "successful execution",
                "effective execution", "selectivity", "optionality",
                "expertise", "awareness", "broader thinking", "client focus",
                "thought leadership", "quest for quality",
                "360-degree thinking", "drill-down", "impetus", "fairness",
                "intellect", "emotional impact", "emotional intelligence",
                "adaptability", "stress management", "self-awareness",
                "strategic thinking", "cross-fertilization", "effectiveness",
                "customer experience", "centerpiece", "SWOT analysis",
                "responsibility", "accountability", "ROI", "line of business",
                "serviceability", "responsiveness", "simplicity",
                "portfolio shaping", "knowledge sharing", "continuity",
                "visual thinking", "interoperability", "compliance",
                "teamwork", "self-efficacy", "decision-making",
                "line-of-sight", "scoping", "line-up", "predictability",
                "recognition", "investor confidence", "competitive advantage",
                "uniformity", "competitiveness", "big picture",
                "resourcefulness", "quality", "upside focus", "sustainability",
                "resiliency", "social sphere", "intuitiveness",
                "effectiveness", "competitiveness", "resourcefulness",
                "informationalization", "role building", "talent retention",
                "innovativeness", "Economic Value Creation",
                "intellectual capital", "high quality",
                "full range of products", "technical strength",
                "quality assurance", "specification quality",
                "market environment", "client perspective",
                "solution orientation", "client satisfaction", "integrity",
                "reputation", "time-to-market", "innovative edge",
                "book value growth", "global network", "ability to deliver",
                "active differentiation", "solid profitability",
                "core capacity", "digital economy",
                "white-collar productivity", "white-collar efficiency",
                "governance", "corporate governance", "business development",
                "corporate identity", "attractiveness", "design philosophy",
                "global footprint", "risk taking", "focus on speed",
                "business equation", "edge", "ownership",
                "competitive success", "discipline", "knowledge management",
                "ability to move fast", "ingenuity", "insightfulness",
                "integrativeness", "customer footprint", "time-to-value",
                "efficacy", "DNA", "dedication", "franchise", "global reach",
                "global touch-base", "technical excellence",
                "values congruence", "purpose", "catalyst for growth",
                "goal setting", "craftsmanship", "operational excellence",
                "re-engineering", "mindfulness", "quality thinking",
                "user experience", "speed of execution", "responsive design",
                'readiness to go "all-in"', "machine intelligence",
                "creativity", "can-do attitude", "relevance", "disruption",
                "dematerialization", "disintermediation", "disaggregation",
                "wave of change", "digitalization", "CAPEX",
                "window of opportunity", "beta", "coopetition",
                "digital change", "business excellence", "business impact",
                "business acumen", "leadership culture", "glocalization",
                "re-equitizing", "cost rationalization",
                "strategic optionality"
            ))

        return inner()
    else:
        if random.randint(1, 287) <= 34:
            return random.choice((
                "key target markets", "style guidelines",
                "key performance indicators", "market conditions",
                "market forces", "market opportunities", "tactics",
                "organizing principles", "interpersonal skills",
                "roles and responsibilities", "cost savings",
                "lessons learned", "client needs", "requests / solutions",
                "mobile strategies", "expectations and allocations",
                "workshops", "dynamics", "options", "aspirations",
                "swim lanes", "pockets of opportunities",
                "social implications", "analytics", "advanced analytics",
                "growth years", "big data", "adjacencies", "core competences",
                "strengths", "corporate values", "core values",
                "competitive dynamics", "workforce adjustments"
            ))

        return make_eventual_plural(inner(), True)


def thing(plural):
    r = random.randint(1, 160)
    if r <= 10:
        return (thing_adjective() + ", " + thing_adjective() + " " +
                thing_atom(plural))
    elif r <= 15:
        return (thing_adjective() + " and " + thing_adjective() + " " +
                thing_atom(plural))
    elif r <= 80:
        return thing_adjective() + " " + thing_atom(plural)
    elif r <= 82:
        return (thing_adjective() + " and/or " + thing_adjective() + " " +
                thing_atom(plural))
    elif r <= 84:
        return growth()
    elif r <= 90:
        return (thing_adjective() + ", " + thing_adjective() + " and " +
                thing_adjective() + " " + thing_atom(plural))
    elif r <= 94:
        return (thing_adjective() + ", " + thing_adjective() + ", " +
                thing_adjective() + " and " + thing_adjective() + " " +
                thing_atom(plural))

    return thing_atom(plural)


def bad_things():
    return random.choice((
        "issues", "intricacies", "organizational diseconomies", "black swans",
        "challenging market conditions", "inefficiencies", "overlaps",
        "known unknowns", "unknown unknowns", "soft cycle issues", "obstacles",
        "surprises", "weaknesses", "threats", "barriers to success",
        "barriers", "shortcomings", "problems", "uncertainties",
        "unfavorable developments", "consumer/agent disconnects",
        "underperforming areas", "information overloads", "concerns",
        "shortfalls", "limitations", "downtimes", "headwinds",
        "subpar returns", "gaps", "market gaps", "pitfalls", "constraints",
        "problems/difficulties", "bottlenecks", "misunderstandings",
        "dilemmas", "interdependencies", "discontinuities", "hiccups",
        "vulnerabilities", "negative cash flows",
        "net profit revenue deficiencies", "negative contributions to profits"
    ))


def eventual_adverb():
    if random.randint(1, 4) == 1:
        return random.choice((
            "interactively", "credibly", "quickly", "proactively", "200%",
            "24/7", "globally", "culturally", "technically", "strategically",
            "swiftly", "cautiously", "expediently", "organically",
            "carefully", "significantly", "conservatively", "adequately",
            "genuinely", "efficiently", "seamlessly", "consistently",
            "diligently", "dramatically", "straightforwardly",
            "differentially", "gradually", "aggressively", "cost-effectively",
            "proactively"
        )) + " "

    return ""


def add_random_article(word, plural):
    r = random.randint(1, 15)
    if r <= 2:
        return "the " + word
    elif r <= 6:
        return "our " + word

    return add_indefinite_article(word, plural)


def eventual_postfixed_adverb():
    plural = random.choice((True, False))
    r = random.randint(1, 235)
    if r <= 34:
        return random.choice((
            " going forward", " within the industry", " across the board",
            " in this space", " from the get-go", " at the end of the day",
            " throughout the organization", " as part of the plan",
            " by thinking outside of the box", " ahead of schedule",
            ", relative to our peers", " on a transitional basis",
            " by expanding boundaries", " by nurturing talent",
            ", as a Tier 1 company", " up-front", " on-the-fly",
            " across our portfolio", " 50/50", " in the marketplace",
            " by thinking and acting beyond boundaries",
            " at the individual, team and organizational level",
            " over the long term", " across geographies", " in the core",
            " across industry sectors", " across the wider Group",
            " by levelling the playing field", " on a day-to-day basis",
            " across boundaries", " within the community",
            " from within the data", " round-the-clock", " moving forward"
        ))
    elif r == 35:
        return " using " + add_random_article(thing(plural), plural)
    elif r == 36:
        return " by leveraging " + add_random_article(thing(plural), plural)
    elif r == 37:
        return (" taking advantage of " +
                add_random_article(thing(plural), plural))
    elif r == 38:
        return " within the " + matrix_or_so()
    elif r == 39:
        return " across the " + make_eventual_plural(matrix_or_so(), True)
    elif r == 40:
        return (" across and beyond the " +
                make_eventual_plural(matrix_or_so(), True))
    elif r == 41:
        return " resulting in " + add_indefinite_article(growth(), False)
    elif r == 42:
        return " reaped from our " + growth()
    elif r == 43:
        return (" as a consequence of " +
                add_indefinite_article(growth(), False))
    elif r == 44:
        return (" because " + add_random_article(thing(plural), plural) + " " +
                build_plural_verb("produce", plural) + " " + growth())
    elif r == 45:
        return " up, down and across the " + matrix_or_so()
    elif r == 45:
        return " ensuring " + add_indefinite_article(thing(plural), plural)
    elif r == 46:
        return (", paving the way for " +
                add_indefinite_article(thing(plural), plural))

    return ""


def person_verb_having_thing_complement(plural, infinitive):
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
        "take a bite out of", "table", "flesh out", "reach out", "jump-start",
        "co-create", "capitalize on", "calibrate", "re-aggregate",
        "articulate", "iterate", "reinvest in", "potentiate", "front-face",
        "co-develop", "take control of", "robustify", "harness", "activate",
        "showcase", "cherry-pick", "digitize", "re-invent", "springboard",
        "solutionize", "re-content", "commoditize", "be eager for",
        "productize", "repurpose", "reenergize", "co-specify", "codify",
        "cross-pollinate", "ignite", "transgenerate", "orchestrate",
        "envisioneer", "reintermediate"
    ))
    if infinitive:
        return inner

    return build_plural_verb(inner, plural)


def person_verb_having_bad_thing_complement(plural):
    inner = random.choice((
        "address", "identify", "avoid", "mitigate", "minimize", "overcome",
        "tackle", "reduce", "alleviate"
    ))
    return build_plural_verb(inner, plural)


def thing_verb_having_thing_complement(plural):
    inner = random.choice((
        "streamline", "interact with", "boost", "generate", "impact",
        "enhance", "leverage", "synergize", "generate", "empower", "enable",
        "prioritize", "transfer", "drive", "result in", "promote",
        "influence", "facilitate", "aggregate", "architect", "cultivate",
        "engage", "structure", "standardize", "accelerate", "deepen",
        "strengthen", "enforce", "foster", "turbocharge", "granularize",
        "operationalize", "reconceptualize", "iterate", "revolutionise",
        "digitize", "solutionize", "lead to", "reenergize", "restructure",
        "cross-pollinate", "ignite", "transgenerate"
    ))
    return build_plural_verb(inner, plural)


def thing_verb_having_person_complement(plural):
    inner = random.choice((
        "motivate", "target", "enable", "drive", "synergize", "empower",
        "prioritize", "incentivise", "inspire", "transfer", "promote",
        "influence", "strengthen", "energize", "invigorate", "reenergize"
    ))
    return build_plural_verb(inner, plural)


def person_verb_and_definite_ending(plural, infinitive):
    if random.randint(1, 106) == 1:
        return ("create an environment where " +
                thing_atom(False) + ", " +
                thing_atom(False) + " and " +
                thing_atom(False) + " can thrive")
    else:
        inner = random.choice((
            "streamline the process", "address the overarching issues",
            "benchmark the portfolio", "manage the cycle",
            "figure out where we come from, where we are going to",
            "maximize the value", "execute the strategy",
            "think out of the box", "think differently", "manage the balance",
            "loop back", "conversate", "go forward together",
            "achieve efficiencies", "deliver", "stay in the mix",
            "stay in the zone", "evolve", "exceed expectations",
            "develop the plan", "develop the blue print for execution",
            "grow and diversify", "fuel changes", "nurture talent",
            "turn every stone", "challenge established ideas",
            "manage the portfolio", "align resources",
            "drive the business forward", "make things happen", "stay ahead",
            "outperform peers", "surge ahead", "manage the downside",
            "stay in the wings", "come to a landing", "shoot it over",
            "move the needle", "connect the dots",
            "connect the dots to the end game", "reset the benchmark",
            "take it offline", "peel the onion", "drill down",
            "get from here to here", "do things differently",
            "stretch the status quo", "challenge the status quo",
            "challenge established ideas", "increase customer satisfaction",
            "enable customer interaction", "manage the balance",
            "turn every stone", "drive revenue", "rise to the challenge",
            "keep it on the radar", "stay on trend", "hunt the business down",
            "push the envelope to the tilt", "execute on priorities",
            "stand out from the crowd", "make the abstract concrete",
            "manage the mix", "grow", "accelerate the strategy",
            "enhance the strength", "create long-term value",
            "meet the challenges", "move the progress forward",
            "do the right projects", "do the projects right",
            "do more with less", "build winning teams",
            "deliver on commitments", "execute", "deliver",
            "see around the corner", "meet the surge", "celebrate the success",
            "circle back", "action forward", "move forward", "take control",
            "be cautiously optimistic", "be committed", "evolve our culture",
            "leverage the benefits of our differentiation",
            "stretch our data bucket", "leapfrog the competition",
            "take the elevator beyond the top floor", "stick to the knitting",
            "bring our vision to reality", "seize opportunities",
            "create momentum", "generate company momentum",
            "pursue new opportunities", "increase adherence",
            "focus on the right things", "open the kimono", "give 110%",
            "take it to the next level", "boil the ocean", "close the loop",
            "create value", "disrupt the status quo"
        ))

    if infinitive:
        return inner

    return build_plural_verb(inner, plural)


def thing_verb_and_definite_ending(plural):
    return build_plural_verb(random.choice((
        "add value", "deliver maximum impact"
    )), plural)


def thing_verb_and_ending(plural):
    compl_sp = random.choice((True, False))

    r = random.randint(1, 102)
    if r <= 55:
        return (thing_verb_having_thing_complement(plural) + " " +
                add_random_article(thing(compl_sp), compl_sp))
    elif r <= 100:
        return (thing_verb_having_person_complement(plural) + " the " +
                person(compl_sp))

    return thing_verb_and_definite_ending(plural)


def person_verb_and_ending(plural, infinitive):
    compl_sp = random.choice((True, False))

    r = random.randint(1, 95)
    if r <= 10:
        return person_verb_and_definite_ending(plural, infinitive)
    elif r <= 15:
        return (person_verb_having_bad_thing_complement(plural) + " " +
                add_random_article(bad_things(), plural))

    return (person_verb_having_thing_complement(plural, infinitive) + " " +
            add_random_article(thing(compl_sp), compl_sp))


def faukon():
    if random.randint(1, 14) <= 13:
        return random.choice((
            "we need to", "we've got to", "the reporting unit should",
            "controlling should", "pursuing this route will enable us to",
            "we will go the extra mile to", "we are working hard to",
            "we continue to work tirelessly and diligently to",
            "we will execute to", "we will sharpen our business models to",
            "to continue our growth, we must", "we are going to",
            "we look forward to working together to"
        ))

    return "we must activate the " + matrix_or_so() + " to"


def person_infinitive_verb_and_ending():
    return person_verb_and_ending(True, True)


def proposition():
    plural = random.choice((True, False))
    r = random.randint(1, 109)
    if r <= 5:
        return (faukon() + " " + person_infinitive_verb_and_ending() +
                eventual_postfixed_adverb())
    elif r <= 50:
        return ("the " + person(plural) + " " + eventual_adverb() +
                person_verb_and_ending(plural, False) +
                eventual_postfixed_adverb())
    elif r <= 97:
        return (add_random_article(thing(plural), plural) + " " +
                eventual_adverb() + thing_verb_and_ending(plural) +
                eventual_postfixed_adverb())
    elif r <= 100:
        return (thing_atom(False) + ", " + thing_atom(False) + " and " +
                thing_atom(False) + " " + eventual_adverb() +
                thing_verb_and_ending(True) + eventual_postfixed_adverb())
    elif r == 101:
        return ("there can be no " + growth_atom() + " until we can achieve " +
                add_indefinite_article(growth(), False))
    elif r == 102:
        return (thing(True) + " challenge us to " +
                person_infinitive_verb_and_ending())
    elif r == 103:
        return thing(False) + " is all about " + thing(plural)
    elif r == 104:
        return "there is no alternative to " + thing_atom(plural)
    elif r == 105:
        return "the key to " + thing_atom(False) + " is " + thing_atom(False)
    elif r == 106:
        return "opting out of " + thing(plural) + " is not a choice"
    elif r == 107:
        return (add_indefinite_article(growth(), False) +
                " goes hand-in-hand with " +
                add_indefinite_article(growth(), False))
    elif r == 108:
        return ("the " + person(plural) + " will be well equipped to " +
                person_infinitive_verb_and_ending())

    return thing_atom(False) + " is a matter of speed of action"


def articulated_propositions():
    r = random.randint(1, 411)
    if r <= 270:
        return proposition()
    elif r <= 280:
        return proposition() + "; this is why " + proposition()
    elif r <= 290:
        return proposition() + "; nevertheless " + proposition()
    elif r <= 300:
        return proposition() + ", whereas " + proposition()
    elif r <= 340:
        return proposition() + ", while " + proposition()
    elif r <= 350:
        return proposition() + ". In the same time, " + proposition()
    elif r <= 360:
        return proposition() + ". As a result, " + proposition()
    elif r <= 370:
        return proposition() + ", whilst " + proposition()
    elif r <= 373:
        return "our gut-feeling is that " + proposition()
    elif r <= 376:
        return ("the point is not merely to " +
                person_infinitive_verb_and_ending() +
                ". The point is to " + person_infinitive_verb_and_ending())
    elif r <= 380:
        p = random.choice((True, False))
        return ("it's not about " + thing_atom(random.choice((True, False))) +
                ". It's about " + add_random_article(thing(p), p))
    elif r <= 383:
        return ("our challenge is not to " +
                person_infinitive_verb_and_ending() +
                ". Our challenge is to " +
                person_infinitive_verb_and_ending())
    elif r <= 386:
        return "going forward, " + proposition()
    elif r <= 389:
        return "actually, " + proposition()
    elif r <= 392:
        return "in the future, " + proposition()
    elif r <= 395:
        return "flat out, " + proposition()
    elif r <= 398:
        return "first and foremost, " + proposition()
    elif r <= 402:
        return ("the game is all about " +
                thing_atom(False) + ", " +
                thing_atom(False) + ", " +
                thing_atom(False) + ", " +
                thing_atom(False) + ", and " +
                thing_atom(False) + " - not " +
                thing_atom(False) + ", " +
                thing_atom(False) + ", " +
                thing_atom(False) + ", " +
                thing_atom(False) + ", and " +
                thing_atom(False))
    elif r == 403:
        return "in today's fast-changing world, " + proposition()
    elif r == 404:
        return "internally and externally, " + proposition()
    elif r == 405:
        return "our message is: " + proposition()
    elif r == 406:
        return "in a data-first world, " + proposition()
    elif r == 407:
        return "the future awaits"
    elif r == 408:
        return (thing_atom(True) +
                " not only thrive on change, they initiate it")
    elif r == 409:
        return ("as the pace of " + thing_atom(random.choice((True, False))) +
                " continues to accelerate, " + thing_atom(False) +
                " has become a necessity")
    elif r == 410:
        return (thing_atom(False) + ", " +
                thing_atom(False) + ", " +
                thing_atom(False) + ", " +
                thing_atom(False) +
                " - all are competing for the attention of " +
                person(True))
    elif r == 411:
        return "success brings success"


def sentence():
    propositions = articulated_propositions()
    return propositions[0].upper() + propositions[1:] + "."


def sentences():
    ret = []
    for _ in range(max(3, int(random.normalvariate(30, 10)))):
        ret.append(sentence())
    return " ".join(ret)


def sentence_guaranteed_amount(count):
    return " ".join(sentence() for i in range(count))


def workshop():
    return sentence_guaranteed_amount(500)


def short_workshop():
    return sentence_guaranteed_amount(5)


def financial_report():
    return sentences()
