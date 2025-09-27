Date: 8.31.25 - Subject: Journal Beginnings. Today I am beginning my SE Journal. On Friday we established git connections and I learned how to setup my SSH Key on GitHub.
Date: 9.5.25 - Subject: Business Architecture. Today we talked about the different roles which need to be filled in typical software businesses. Here are 2 things he said to remember:
	1. Someone who understands AND can communicate the requirements.
	2. Smart people who can build what the requirements specify.
These make up 80-90% of what the business needs. A couple notes about how to work effectively with product owners:
	- These people determine what you are going to build - you want to help them.
	- Learn how to ask good questions. Get them to tell you what they think and then read it back to them. Draw pictures of what they describe.
Million dollar advice for project managers: Try hard to make good estimations, pad your time, and get your stuff done. 
Architects: Let them see your problems.
Peer Engineers: Leave your ego at the door and look for ways to be helpful.
UX: Often don't understand the nature of software development. 
Reminder of what DevOps is: 
	Someone who is tightly involved with the development stuff and tightly 
	involved in the operation of the stuff. Worries about security, tech 
	stack, infrastructure, scalability, etc.
Date: 9.12.25 - Subject: User Stories. 
	"Agile Development" - almost universal to use user stories to track their work items.
	1. A description of the OUTCOME of a small unit of work.
	"As a 'lighthearted social media user' I want 'to log into ___' so that 'I can have low key interactions with other lighthearted people'."
	Writing requirements this way gives a common language for people to understand, even if they never had contact with the person who wrote it. You can even have a non-person be the user in the statement (As the storage module, I want...). 
	We can also use user stories as points of measurement, using the Fibonacci sequence: 2,3,5,8,13,21. Then we add up all the points of our stories, define the time range to complete them, then we can see how many points we need to acheive each day to keep pace. "Burndown chart" 	
Date: 9.17.25 - Subject: Design Patterns. Multiple servers, one queue: Grocery store self checkout lines. What these patterns look like in real life:
	A recipe is a pattern, follow a series of steps. This could be building Ikea furniture or getting step-by-step directions to get somewhere. 
	What is the difference between a pattern and an algorithm? An algorithm is an application to a set of steps to a problem. A design pattern is more abstract. A pattern could be telling someone to follow a recipe, whereas an algorithm is a very specific series of steps to accomplish something.
	Professor Compas recommended that we find people who create content about our fields that we like. 
	"What is a design pattern?" It's my birthday tomorrow and my wife will bake a cake for me. The recipe she follows is an alogrithm - specific steps to create the same cake over and over again, if repeated. The birthday party is a design pattern, something where everyone may picture a little bit differently, but it is still recognizable as a birthday party. Say you have 5 cake recipes in your database. They follow very similiar steps, but will be slightly different. The design pattern for making the cakes are the same, but each cake has it's own algorithm. For each cake, you still need to get ingredients, mix them up, and bake them. 
	Observer pattern: You have a list of people who are interested (subscribers). Obviously you need a subscribe method which takes in some information. That builds the subscribers list. Then, whenever you want to notify them, you loop through the list and use the gathered information to send notifications. 
	Singleton pattern: Create a sealed class which means no other instances of the class can be created. 
	Facade pattern: You have a class which does something. In order to use it, you need to pass it a whole bunch of paramters. Instead of directly calling the class or function, you use a facade pattern which has different functions that filters them and calls the root function in the way it should. 
	Synchronous: in order. It goes 1, 2, 3, 4... while Asynchronous happens simultaneously. It goes maybe 1, 4, 3, 2, at the same time, disconnected from each other. 
Date: 9.19.25. Subject: Diagramming. 
	Flow and component diagrams are what we will focus on. 
	
	Flow diagram: Helps us think through how the data or processes go in our system.
	Component diagram: What are the major building blocks of our system and how do they relate to each other?

Example process:
	1. User searches for an item "Lamar Jackson jersey"
	2. User recieves list of matching items
	3. Users scrolls through options
	4. User clicks on an item to look at more closely
	5. User decides to buy the item
	6. Add item to cart
	7. Continue shopping?
	8. Verify payment info
	9. Verify shipping info
	10. Payment accepted?
	11. Deduct from inventory
	12. Handle shipping
(This is an example of a design pattern as well)

	Use draw.io, use circles to indicate starts and stops, connect sections by using matching numbers. Decisions ask 'yes' or 'no', they have exactly two paths. Simple processes have as many options going into it, but only one going out (round boxes). 
Date: 9.22.25. Subject: Pitch deck. 
	Impactful presentation keys: 
		1. Who's the audience?
		2. What are the goals?
		3. Follow design principles
	Design elements: Text size, color, and element size are all important. Bold and italics help draw attention to key ideas. Color can convey all kinds of information. Size and count of elements change the emphasis of the page. 5-9 is the sweet spot for elements on a slide. Information density is a critical consideration. Pictures tell a 1,000 words. Good pictures can tell 10,000.
	Color can:
		1. Communicate emotion and evoke feelings
		2. Highligh elements
		3. ...
	Red is for some kind of ALERT.
	Yellow is for highlighting changes or new things
	Green is for good things or familiar things
	Gray is for out of scopre or not of consequence
	Blue for neutral or existing things
	Orange to pay attention or for things that are changing
	"The world according to Jeff. ^"
	Coming back to central ideas can really help to cement the ideas in people's minds.
	 
Date: 9.26.25. Subject: Pitch deck.
	The legionaries went out an had a meeting in the whiteboard room by room 116. We hashed some things out and made solid progress on the presentation. I tried to get everyone to coordinate so our presentation looked professional but no one listened. I may have to restyle some things once people have done their slides.
