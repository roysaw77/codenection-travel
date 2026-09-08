# Travel Planner Hackathon - Ideation Record

> Status: prototype-phase concept exploration. This document records the ideas discussed so the team can compare them before selecting the final product direction.

## 1. Challenge Context

Trip planning is fragmented across booking platforms, maps, budgeting tools, itineraries, and group chats. Travellers have different budgets, schedules, interests, dietary requirements, mobility needs, and travel styles. These differences become harder to coordinate in a group, and an itinerary can quickly become unusable when weather, delays, closures, or personal needs change.

The hackathon challenge asks for a solution that helps travellers plan from start to finish, including budgeting, itinerary creation, group preference coordination, and adjustment when plans change.

## 2. Initial Problem Statement

Travel information is widely available, but most recommendations are generic and do not precisely match a particular traveller or group. Students, couples, families, and friend groups have different constraints and expectations. Existing planning processes also become stressful when information is scattered across applications or when a change forces the organiser to rebuild the itinerary manually.

## 3. Ideas Discussed

The creativity scores below are internal estimates based only on the hackathon's 15-point Creativity and Novelty category. They are not official judging scores.

| Idea | Main concept | Originality /7 | Novel features /5 | Differentiation /3 | Estimated total /15 | Decision |
|---|---|---:|---:|---:|---:|---|
| A. Personalized AI Travel Planner | Generate an itinerary from a user's target group, budget, interests, and natural-language request | 2 | 1 | 1 | **4** | Drop as the headline; retain as basic infrastructure |
| B. Conversational Replanner | Let users modify an itinerary through natural language when their plans change | 2 | 2 | 1 | **5** | Retain as supporting functionality |
| C. AI Group-Chat Summarizer | Provide a Discord-style trip discussion where AI records the conversation, summarizes preferences, and generates a group itinerary | 2 | 2 | 1 | **5** | Do not use alone; close competitors already exist |
| D. Living Trip Memory | Convert chat messages into confirmed constraints, preferences, decisions, rejected suggestions, unresolved questions, and booking commitments | 3 | 3 | 2 | **8** | Retain as a supporting system |
| E. TripPact / Trip Constitution | Detect conflicts between group members, explain trade-offs, facilitate voting, and produce a fair itinerary | 3 | 3 | 1 | **7** | Retain selected mechanics; do not use as the sole novelty |
| F. Minimum-Disruption Replanning | Change only the affected parts of a trip while preserving bookings, budget limits, hard constraints, and must-have activities | 3 | 3 | 2 | **8** | Retain for the disruption prototype flow |
| G. ParallelTrip | Generate synchronized subgroup itineraries so members can separate for incompatible activities and reunite at optimized anchor points | 6 | 5 | 3 | **14** | **Chosen as the core concept** |

## 4. Idea A - Personalized AI Travel Planner

### Concept

The user describes a destination, budget, dates, group type, interests, and preferred travel style. AI generates a suitable itinerary.

### Proposed features

- Personalized itinerary generation
- Student, couple, family, or solo profiles
- Budget and activity suggestions
- Natural-language input
- Map with distance, price, and ETA
- Trip reminders
- Natural-language itinerary editing

### Strengths

- Directly addresses the challenge statement
- Easy for users and judges to understand
- Feasible to demonstrate in a prototype

### Weaknesses

- AI itinerary generation is already common
- Broad personas create a weak target-market story
- Maps, reminders, prices, and chat editing are expected features rather than a defining innovation
- It would be difficult to explain why users should choose it instead of Trip.com or another established planner

### Decision

Do not present this as the innovation. These capabilities can support the final product, but they cannot be its main selling point.

## 5. Idea B - Conversational Replanner

### Concept

Users modify the plan through natural language, for example:

> It started raining. Move the outdoor activities to tomorrow, keep tonight's market, and do not exceed RM250 per person.

### Strengths

- Natural interaction during a stressful disruption
- Demonstrates that the product remains useful after the initial planning stage
- Can create a strong before-and-after prototype moment

### Weaknesses

- Replanning, weather alternatives, and conversational editing already exist in travel products
- A completely regenerated itinerary may ignore earlier group decisions
- Real-time availability and reliable pricing could make the prototype scope unrealistic

### Decision

Retain replanning, but make it preserve decisions and change as little as possible.

## 6. Idea C - AI Group-Chat Summarizer

### Concept

Create a Discord-inspired trip workspace where friends discuss the trip. AI follows the discussion, summarizes it, and generates an itinerary.

### Possible interface

- Trip channels such as `#general`, `#itinerary`, `#expenses`, and `#announcements`
- Main group conversation
- AI assistant inside the discussion
- Live trip-summary panel
- Shared map and itinerary

### Strengths

- Familiar group interaction
- Reduces the need to complete long preference forms
- Preserves context that is normally lost in WhatsApp or another chat application

### Weaknesses

- Several products already turn group chats into itineraries
- Summarization alone does not resolve disagreements
- AI may incorrectly treat a casual suggestion as a confirmed decision
- Copying Discord's appearance too closely could make the product feel derivative

### Decision

The discussion space can be the input experience, but it must not be presented as the central innovation.

## 7. Idea D - Living Trip Memory and Decision Ledger

### Concept

Instead of storing only chat messages, the AI maintains structured group knowledge.

### Information recorded

- Hard constraints that cannot be violated
- Soft preferences that can be negotiated
- Each person's must-have activity
- Confirmed group decisions
- Ideas still awaiting a decision
- Rejected ideas and the reason for rejection
- Bookings that should be locked
- Budget commitments
- Unresolved conflicts

### Confirmation rule

The AI should not silently convert every message into a final requirement. It asks for confirmation when meaning matters:

> I interpreted RM250 as Amy's maximum total budget. Should I save it as a hard constraint?

### Value

The itinerary remains connected to the reasons behind it. During replanning, the system knows which decisions must be protected and avoids repeatedly suggesting rejected ideas.

### Decision

Retain this as the intelligence layer behind the chosen concept.

## 8. Idea E - TripPact and the Trip Constitution

### Concept

TripPact acts as a neutral group facilitator. It converts individual requirements into a shared Trip Constitution, detects incompatible requests, and presents understandable compromises.

### Example conflict

```text
Amy: Maximum budget of RM250
Ben: Theme park is a must-have
Estimated plan: RM327 per person

Conflict: the current plan violates Amy's hard budget limit.
```

### Example resolution card

```text
A. Keep the theme park: RM327/person
B. Replace it with a lower-cost activity: RM238/person
C. Let the group separate temporarily: RM240-RM327/person
```

The group can vote, confirm the decision, and store its reasoning in the decision ledger.

### Fairness-ledger variation

If one member gives up a highly valued activity, future decisions can give additional weight to that member's remaining preferences. This prevents the loudest participant from controlling the whole trip.

### Strengths

- Tackles disagreement rather than only recommendation
- Makes AI decisions more transparent
- Provides a convincing group-planning story

### Weaknesses

- Newer competitors are beginning to offer AI mediation, constraints, and fair group planning
- Fairness is subjective and may be difficult to explain clearly
- Voting can still force every person into one mediocre shared itinerary

### Decision

Keep constraint confirmation, conflict detection, and decision cards. Replace the assumption that every conflict must end in one shared activity.

## 9. Idea F - Minimum-Disruption Replanning

### Concept

When a disruption occurs, the system repairs the itinerary instead of generating a completely new one.

### Protected information

- Completed activities
- Confirmed bookings
- Hard constraints
- Remaining group and personal budgets
- Must-have experiences
- Meeting commitments
- Decisions already accepted by the group

### Example output

```text
Changed
- Beach moved to tomorrow morning
- Indoor museum moved to 2:30 PM
- Bus replaced with Grab: +RM7/person

Preserved
- Night market
- Halal dinner
- Return before 8:00 PM
- Total budget remains below RM250
```

### Decision

Retain as an important supporting feature. The prototype only needs one convincing disruption scenario rather than complete real-time travel coverage.

## 10. Idea G - ParallelTrip

### Core insight

Most group planners assume that one group needs one itinerary. In reality, forcing everyone into the same schedule creates unnecessary compromise. ParallelTrip determines when the group should be together, when it can separate, and how everyone can reunite without coordination stress.

### One-sentence concept

> ParallelTrip converts a group discussion into synchronized personal or subgroup itineraries organized around shared anchor moments.

### Planning model

```text
Shared breakfast
       |
       +----------------------+----------------------+
       |                                             |
Adventure track                               Relaxed track
Hiking and nature                             Cafe and museum
Amy and Ben                                   Chloe and Dan
       |                                             |
       +----------------------+----------------------+
                              |
                  AI-optimized reunion point
                              |
                       Shared halal lunch
```

### Key concepts

#### Shared anchors

Activities everyone wants or needs to attend, such as a booked dinner, hotel check-in, transport departure, or sunset experience.

#### Fork windows

Periods when the group can safely separate based on different interests, budgets, mobility, pace, or energy.

#### Parallel tracks

Different mini-itineraries generated for individuals or subgroups. Each track has its own route, cost, timing, and activities.

#### Optimized reunion points

Meeting locations selected using travel time, cost, accessibility, dietary requirements, opening hours, delay risk, and the next shared activity.

#### Buddy and safety constraints

Rules such as "nobody travels alone," "a child must remain with a parent," or "this member requires an accessible route."

#### Live track switching

A traveller can move to a different track. The system explains the transport route, timing, ticket consequences, and whether anyone would be left alone.

#### Cross-track disruption recovery

If one subgroup is delayed, the system adjusts the reunion or gives the other subgroup a short nearby activity without rebuilding the entire trip.

### Why it is different

Conventional group planners try to find one option everyone will tolerate. ParallelTrip treats temporary separation as a valid planning tool and automatically coordinates the reunion. The distinctive combination is:

- Natural group discussion as input
- Automatic detection of incompatible preferences
- AI-generated subgroup formation
- Synchronized parallel itineraries
- Optimized reunion locations and times
- Safety and buddy rules
- Live cross-track replanning

### Risks

- The product must not make splitting up feel antisocial
- Subgroup recommendations must respect safety and accessibility
- Route and ETA calculations need reliable map data
- The team must avoid building a full booking platform during the prototype phase

## 11. Overall Recommendation

### Chosen concept

**ParallelTrip with Living Trip Memory and minimum-disruption recovery**

The final concept should not combine every explored feature equally. Its hierarchy should remain clear:

1. **Core innovation:** synchronized split-and-reunite itineraries
2. **Input method:** group discussion and private preference capture
3. **Intelligence layer:** confirmed constraints and decision memory
4. **Supporting mechanism:** conflict explanation and decision cards
5. **Recovery mechanism:** minimum-disruption replanning
6. **Infrastructure:** map, ETA, estimated costs, and reminders

### Final value proposition

> Other travel planners ask, "What can everyone tolerate doing together?" ParallelTrip determines when the group should be together, when members should follow different experiences, and how they can reunite effortlessly.

### Recommended target group

Start with groups of **3-6 budget-conscious university students planning short trips**. This target has clear budget conflicts, different interests, transport constraints, and a familiar group-chat planning problem. Couples, families, and solo travellers can be future markets, but they should not weaken the initial pitch.

## 12. Recommended Prototype Story

Use one destination and one group throughout the prototype.

### Scenario

Four university students are planning a two-day Penang trip:

- Amy has a maximum budget of RM250
- Ben wants to hike
- Chloe has an injured ankle
- Dan wants street photography
- Nobody wants to travel alone
- Everyone wants halal lunch and the sunset together

### Six-screen core flow

1. **Create the trip** - destination, dates, group, and budget
2. **Group discussion** - members describe preferences naturally
3. **Trip Memory** - AI asks members to confirm extracted constraints
4. **Conflict insight** - AI explains why one shared route performs poorly
5. **Parallel plan** - two tracks appear on the map and converge at lunch
6. **Disruption recovery** - rain delays one track and AI resynchronizes the reunion

### Success indicators displayed in the prototype

- Hard constraints satisfied
- Personal and group cost
- Time spent together versus in subgroup tracks
- Estimated walking and travel time
- Reunion confidence or delay risk
- Number of unresolved decisions

## 13. MVP Scope

### Build for the prototype

- One destination dataset
- One scripted group scenario
- Group discussion interface
- AI extraction into structured constraints
- Confirm or correct extracted requirements
- Two generated parallel tracks
- Map visualization with one reunion point
- Cost and ETA comparison
- One disruption and resynchronization flow
- Clear explanation of what changed and why

### Mock or defer

- Real booking and payment
- Worldwide destination coverage
- Continuous live flight monitoring
- Production-grade WhatsApp or Telegram integration
- Automated refunds or cancellations
- Complex expense settlement
- Full notification system
- Unlimited dynamic subgroup combinations

## 14. Technical Principle

Use the language model for understanding and explanation, not as the source of factual truth.

```text
Group messages
    |
Language model extracts proposed constraints and preferences
    |
Users confirm or correct important facts
    |
Constraint and scheduling engine creates anchors and fork windows
    |
Map/place data provides routes, ETA, and location information
    |
Optimizer generates synchronized parallel tracks
    |
Language model explains the result and proposed changes
```

Costs, opening hours, travel times, locked bookings, and hard-constraint validation should come from structured data or deterministic logic wherever possible.

## 15. Presentation Positioning

### Problem hook

> Group travel does not fail because people lack recommendations. It fails because people want different experiences but traditional planners force them into one schedule.

### Product pitch

> ParallelTrip turns a messy group conversation into coordinated shared and personal experiences. It protects the moments everyone wants together, creates synchronized routes when preferences conflict, and brings everyone back together at the right place and time.

### Differentiation statement

Avoid claiming that this is the first idea of its kind. A defensible statement is:

> Unlike conventional group planners that produce one shared itinerary, ParallelTrip generates synchronized subgroup experiences around optimized reunion points.

## 16. Next Validation Questions

Before finalizing the concept, test these assumptions with potential student travellers and a mentor:

1. Are groups comfortable separating during a trip?
2. What activities must always remain shared?
3. What makes a reunion point feel safe and convenient?
4. Would users trust AI to form subgroups automatically, or should they confirm them?
5. Which matters most during replanning: budget, preserving booked activities, or arriving together?
6. Does a split-and-reunite plan reduce conflict compared with voting on one itinerary?

The answers should determine whether ParallelTrip remains the final direction or requires another iteration.
