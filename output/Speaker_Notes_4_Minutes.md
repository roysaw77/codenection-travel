# Four-minute presentation script

## Slide 1

Timing: 20 seconds.
Senior Travel Companion helps adult children support older parents when they cannot travel together. We focus on parents aged sixty and above who join organised tours. The child helps choose the trip, the parent uses a simple interface, and the guide provides local support. This is our proposed product, illustrated through a UI prototype.

## Slide 2

Timing: 30 seconds.
Imagine a daughter arranging a holiday for her mother, who prefers short walks. A tour listing may look suitable, but she still needs to understand walking demands and the evidence behind the operator. During the trip, a missed reply gives little context. The parent also needs a simple way to ask for help. These are hypotheses we will validate through family and guide interviews.

## Slide 3

Timing: 40 seconds.
The child enters a parent profile with walking tolerance, rest needs, language and budget. The proposed matcher compares it with tour, guide, itinerary and safety information. Explicit rules calculate suitability, while the AI advisor explains the fit and missing information. For example, a forty-minute walk should be flagged for a parent who prefers twenty minutes. The Trust Profile shows supporting evidence and review status. Our displayed scores are fixed demo values, and neither suitability nor a trust profile guarantees safety.

## Slide 4

Timing: 35 seconds.
Parents should not need to learn a complex dashboard. Senior Simple Mode brings the next stop and meeting details to the main screen. The largest action lets them say I am okay. Calling the guide and requesting help remain easy to find. We use short labels and prominent controls, with detailed planning in the child view. We still need usability testing with older adults, including text scaling and whether users understand the help actions.

## Slide 5

Timing: 35 seconds.
The child dashboard combines the itinerary with the latest check-in and a future trip map. The map concept shows the parent’s consented shared location, the next stop and the update time. It uses an illustrative map in this prototype and has no live tracking. If a parent requests rest or sends SOS, the proposed alert workflow contacts the authorised guide and child. The guide can respond locally while the child supports remotely. The app must show stale data and separate acknowledgements. These screenshots simulate the workflow. They do not send notifications or provide emergency response.

## Slide 6

Timing: 30 seconds.
Existing products already solve useful parts of this problem. TourRadar offers senior tours and physical ratings. TripIt organises and shares itineraries. Life360 supports location sharing and SOS. Our proposed difference is joining parent-specific tour selection with support during travel, connecting the parent, child and guide. We are not claiming these individual features are unique. We need to validate whether this connected workflow matters enough for families to adopt and pay for.

## Slide 7

Timing: 30 seconds.
Our planned frontend is Flutter, backed by FastAPI and Supabase for profiles, trips and permissions. LangChain sends relevant evidence to NVIDIA NIM to explain matches. Backend rules control scoring and alerts. For routing, Geoapify is a lower-cost MVP candidate, subject to local coverage tests. FCM and a persistent worker handle notifications and overdue events. The existing demo uses HTML, CSS and JavaScript. These integrations are planned, and we will confirm provider limits before implementation.

## Slide 8

Timing: 20 seconds.
Our next milestone is one working trip across two devices: a child creates a profile, reviews a match and receives a parent check-in. Then we test guide acknowledgement and usability with older adults. Today we have the interface concept. Our goal is to help families choose a suitable tour and stay connected when they cannot travel together.