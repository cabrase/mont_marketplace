# Mont Marketplace
### Westmont CS Capstone Project
#### Author: Carson Brase | cabrase@gmail.com
#### Professor: Mike Ryu | mryu@westmont.edu

## Table of Contents

- [Description](#description)
- [Problem](#problem-to-be-solved)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [License](#license)

## Description
Mont Marketplace is a web-based application made exclusively for the Westmont community. It enables students, faculty, 
and staff to easily buy and sell a broad range of used items and services within the safety and convenience of 
Westmont’s campus. With an intuitive and appealing interface, users are able to create an account, post listings for 
items or services they wish to sell, and view countless items for sale from others on the site. From furniture to 
surfboards to textbooks, Mont Marketplace caters to a variety of needs and fosters a culture of sustainability through 
reuse and exchange on campus.

## Problem to be Solved
You may be thinking, "What's the point of this? Websites like Craigslist and OfferUp already exist!" However, as 
wonderful as these used-goods websites can be, they come with costs and risks. First, they require meeting a complete
stranger somewhere in public, which can be nerve racking and bring up questions of safety. Additionally, both the buyer 
and seller must drive to the meeting location, incurring the costs of gas to get there and inconvenience of leaving 
one’s home. Next, the public exchange of money adds to safety concerns, which are only heightened for more expensive 
items. Lastly, these sites have the unfortunate side effect of scammers seeking to steal personal information. For these
reasons and more, many Westmont students will abstain from selling their items on sites like Craigslist and OfferUp.

So, what happens to these items? More often than not, they end up in dumpsters outside the Westmont dorms and 
eventually make their way to the local Santa Barbara landfill. A college campus generates an immense amount of waste, so
it is crucial that everyone does their best to reduce their environmental impact to create a more sustainable community.

## Features
- **User Authentication**: Only Westmont College students, faculty, and staff can register and create accounts using their official college credentials.
- **Listings**: Students can create listings for items they want to sell. Each listing includes details such as title, description, price, condition, and seller information.
- **Search and Filter**: Users can easily search for specific items or filter listings based on categories, price range, and item condition.
- **Profile Management**: Users can manage their profiles, update contact information, and view their listings.

## Technologies Used
- **Django (python)**: A Python web development framework that will be used for backend development of Mont Marketplace. 
Django’s built-in user authentication system will serve as the cornerstone of this project’s novelty, providing the 
framework for users to log in to their personal profiles to post items for sale.
- **SQLite**: Used by Django for creating models (ie: User, Listing, etc.) and database management. These models 
will serve as the foundation for the site, containing the structure of each user profile and listing that is posted. 
- **HTML, CSS, Javascript, Bootstrap**: Used for front-end development and user interface design within Django. The 
combination of these four tools will contribute to the layout, function, and intuitiveness of the site. Bootstrap will
be used for forms, buttons, navigation, and other important parts of the user interface.

## Getting Started
To get started with Mont Marketplace, follow these steps:

1. **Register**: Sign up for an account using your Westmont College email address and complete the registration process.
2. **Browse Listings**: Browse the listings to find items you're interested in purchasing.
3. **Create Listings**: If you have items to sell, create listings providing accurate descriptions and images.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
