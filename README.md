# Cards Against Humanity
> Play CAH directly in your browser with the power of WebRTC

## Play in your browser
*Note: link will be added soon*
1. Ask the host (black card reader) to visit [this link]()
2. Ask the host to copy and send the link generated
3. The players should automatically connect to the game

Mobile devices recommended

## To do
- [x] Shuffle cards. Currently, all users will get the same hand of white cards. The order of black cards is also the same.
- [ ] Find a way to "shuffle the deck and distribute cards" throught the sockets. Even when the cards are shuffled, there's a probability that two players get the same white cards. This will be a lot more difficult to fix.

## Built with
- NodeJS + Express
- Socket.IO
- HTML/CSS/JS (no frameworks)
- [JSON Against Humanity](https://www.crhallberg.com/cah/) (Using the base set)
- PeerJS
- Python (to generate arrays for the white and black cards)

## How does this work?
1. A peer ID is generated 
2. (to be completed)

## License
GNU AGPLv3