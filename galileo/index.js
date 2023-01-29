const twilio = require('twilio')
const session = require('express-session')
const express = require('express')
require('dotenv').config()

const{MessagingResponse} = require('twilio').twiml
const{Configuration,OpenAIApi} = require('openai')

const app = express()
const client = twilio();
const port = 3130


client.api.accounts
  .create({
    friendlyName: 'HOYAHACKS'
  })
  .then(account => {
    console.log(account.sid);
  })
  .catch(error => {
    console.log(error);
  });

app.use(express.urlencoded({extended:true}))
app.use(session({
    secret:'chattwil',
    resave:'false',
    saveUnitialized: true,
    cookie:{}
}))

const configuration = new Configuration({
    apiKey: ''
})

const openai = new OpenAIApi(configuration)

app.post('/bot', async(req,res)=>{
  const twiml = new MessagingResponse()
    if (!req.session.init) {
        twiml.message('Welcome! Reply with three comma separated adjectives describing your preferred AI chatbot.');
        req.session.init = true;
        res.type('text/xml').send(twiml.toString());
        return;
      } 
      if (!req.session.personality) {
        req.session.personality = req.body.Body.toLowerCase();
        twiml.message('Whats your name?');
        res.type('text/xml').send(twiml.toString());
        return;
      }
    if(!req.session.name){
        req.session.name = req.body.Body
    }      
    if (!req.session.prompt) {
        req.session.prompt = `The following is a conversation between a human and their new AI best friend who is ${req.session.personality} and is very into astronomy. Human: Hello, my name is ${req.session.name}. AI:`;
      } else {
        const reply = req.body.Body.trim();
        req.session.prompt += `Human: ${reply}. AI:`;
      }
      const response = await openai.createCompletion({
        model: "text-davinci-002",
        prompt: req.session.prompt,
        temperature: .9,
        max_tokens: 2048
      });
      
      const bot = response.data.choices[0].text.trim();
      req.session.prompt += `${bot}`;
      twiml.message(bot);
      
      res.type('text/xml').send(twiml.toString());
            
})

app.listen(port, () => {
    console.log(`AI friend app listening on port ${port}`)
  });
  