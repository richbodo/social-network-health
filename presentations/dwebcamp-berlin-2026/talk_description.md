
## Title


## Summary

The root of our social graph is personal contact data and private relationship data - for most, that data is spread across a half-dozen SaaS vendors who pollute it and make it difficult to use.  Bringing that root local is a massive personal and community health unlock.  

This effort is underserved, high leverage, and just the beginning of what is only recently possible to explore and implement.  

I am engaged in ongoing context development around community health for my communities.  To make that useful, I built a toolkit.  We'll run it against a popular open source application that handles contact data - to evaluate it's safety and efficacy as an application that deals with our personal contact and relationship data.

Then we will discuss plan to help our communities take control of their contact and relationship data, and gain meaningful insights from that data to improve community health.

Then we will workshop our own applications - or any application that handles personal relationship data that we would like to cover - evaluating them for safety and efficacy in supporting personal network health.  If we have time or the group wants more discussion - we can discuss future directions  for this type of validation methodology to any depth - even if it is preferred to workshopping our own tools.

## Detailed description

Here’s the plan - At a high level - I will present a proposed architecture for each of these steps, and show my progress to date for each of the three steps in the plan, demo the tools, and we will then workshop against our own applications, or our favorite ones:

This is the long-term plan I will present: 

First, Take back the Root:

I built an agent-ready Toolkit for credible interop between local-first and SaaS systems that can move someone's personal network root local, away from SaaS.  I have built reference designs that are in use by my communities, and they are regularly validated against an architectural spec that I will briefly describe.

The Toolkit has four goals:  1) Take ownership of the Root of our personal networks - 2) Protect the Root’s integrity by software validation - 3) Protect the Root from unwanted egress - and 4) Protect the Root from entropy and accidents.  From those goals, architectural commitments fall out into the spec.

The premise is that by validating the safety of the software and data we use to contact others, we can increase confidence in doing so, and protect our data from the whims of ever-changing centralized organizations.  This is a method for ongoing context development around our digital infrastructure and community health.

Building a safe local environment for the Root also makes private relationship data (i.e. who do I call for help with sensitive health issues) first class, where entering that data into SaaS was never even a consideration.  Private relationship data becomes the more important layer on top of contact data - a layer which must never egress.  

Ready use of a well organized personal network root also ensures that we can help-seek and provide help without being drowned in SaaS noise first.  These are huge wins.

Once we have our contact and relationship data local, we can gain insights from our egocentric social graphs (the sociogram with us at the center) right away, categorizing our personal relationships by function (what group do I talk to about x?).  

As grounded members of our personal networks, we can encourage others to Free the Root better than anyone outside our networks - giving our communities a strong sense of safety and utility with that data.  We can deliver home-cooked software meals that serve our communities' needs exactly, where centralized systems cannot.

Second, Add communications analysis to our private relationship data:

Adding communications data can supercharge our local-first apps, but it requires a safe environment for enhancing our Private Relationship Layer on top of our contact data, pulling communications data out of SaaS (Gmail, Whatsapp, etc.).  

Examples of insights we can gain by adding personal communications to the private relationship layer on top of the Root are things like: Support Coverage: Do I have people for the kinds of help I need?  Resilience: If one person becomes unavailable, what breaks?

This step is mechanically similar to the Taking Back the Root, and it will be well served by the same architectural commitments.  No egress is required, and yet more data is taken back from SaaS systems to become canonical in the local environment, and more value is achieved by adding personal relationship data that has no business every egressing our local systems to SaaS.

Third, design interventions from egocentric data sets:

This is where we threat model,  develop and exhaustively test, and engage researchers prior to deployment.  Threat modelling is an ongoing process that this project pays attention to.

I will identify several opportunities to make a real impact - based on productive research that has never been implemented for remote digital-first communities.  These all exist at the same level of sensitivity and can be implemented in parallel, but should not pass through the distribution gate without qualified research input.

Opportunity 0: Education around help-seeking and community health

We can learn a lot from Social Network Health research in other contexts.  Our digital infrastructure can be instrumented to supply us with best practices when we need them the most.

Opportunity 1: Macrostructure from Microstructure - community analytics:

Research in social network health has proposed methods of generating sociocentric data by combining data from egocentric graphs.  We know we can share our personal network information with each other to achieve insights into our community - but if we want to protect the data that is shared, we have to do a little math.

Modern cryptographic systems give us a way to test methods from social network health research in ways that have not been possible before.   We can develop actionable insights by combining data from our own egocentric networks, if we’re smart, without aggregating any identifying information until necessary - remotely!

This end-runs the typical intervention methods that aggregate re-identified data sets - gathering sensitive data from an entire community into one place - making this far less difficult and dangerous, at the up-front cost of building complex software systems.

The types of things we can identify from social network analysis of this kind:  Binned degree distribution - are many people isolated or overloaded?  Support/advice concentration - is too much support load falling on a few people?, and much more.

This requires implementing papers that have never been implemented with brand new tech, threat modeling and exhaustive testing.  It’s a big, longer-term project, but I believe it’s possible to pull it off.

Opportunity 2: Connection Requests with Staged Disclosure - Engaging broader communities 

A protocol for reaching beyond a users egocentric network into communities that opt-in provides access to members of larger communities (i.e. a signal group) for members of that group that opt-in.  Fallbacks are pre-generated to handle failure of this larger outreach.

Ultimately, this protocol (for now the SNH Notification Protocol) could be combined with analysis triggers to automate outreach in some situations.

As soon as I present the architecture and progress for each step, we will break out into groups and red/blue team the architecture and ideas, synthesizing our finding at the end of the session.

History

After my last talk at DWebCamp, I was approached by someone who suggested I should build an app to improve mental health in the developer community. Having followed probably the best social network health trainer alive for about five years, I did not think that would work at all. Later I had my own mental health challenge and tried to use SaaS systems to find people to talk to urgently. I was met with noise, distraction, and a long traversal through people I did not really know, until I ran out of energy. Right then I realized I had to get control of my contact data - I could not survive that kind of thing - I need to know who is important and who I can talk to when I have no energy at all and need a friendly human.

After implementing a paper solution, then building a couple command line contact managers and a directory archive for myself, and after studying social network health specifically for remote workers, I started to see the local-first light. I was using my own apps more than SaaS apps to discover and reach out to friends - only my phone competed with them. I cannot realistically exit SaaS, but I can interoperate with it now, without distraction, and I control all of my private relationship data.
Then after reading Smith (Macrostructure from Microstructure: Generating Whole Systems from Ego Networks.) I realized that there is far more to this effort, and that the possibility exists for remote workers to combine forces to help their own communities.

Who this workshop is for:

Spec-curious builders, local-first folks, anyone who's tried and failed to exit their contacts from SaaS, ATProto people thinking about the private-data gap. Anyone in a bigger project that is wondering what projects that are mostly constrained to one person's bandwidth, building home-cooked software meals, are coming up with in this space. People who want to know what is possible when attempting to improve the social network health of their communities, using modern tech, and what is on the horizon.

Agenda:

Background + SNH framing + Prior Art (5 minutes):
Demo (5 minutes):
Three part plan - Architecture Walk-Through (15 minutes of highlights):
Validate apps, critique plan, and rework in small groups (25 minutes):
Wrap - what survived (10 minutes):


