const Discord = require('discord.js');

const client = new Discord.Client();

const prefix = '>';

const fs = require('fs');

client.commands = new Discord.Collection();

const commandFiles = fs.readdirSync('./commands/').filter(file => file.endsWith('.js'));
for (const file of commandFiles) {
    const command = require(`./commands/${file}`)

    client.commands.set(command.name, command);
}

client.once('ready', () => {
    console.log('UIUC Covid bot is online');
});

client.on('message', message => {
    if (!message.content.startsWith(prefix) || message.author.bot) return;

    const args = message.content.slice(prefix.length).split(/ + /);
    const command = args.shift().toLowerCase();

    if (command === 'deez') {
        client.commands.get('deez').execute(message, args);
    } else if (command === 'data') {
        client.commands.get('data').execute(message, args, Discord);
    }
})

client.login('Nzk1NzEwNDU2Mjk1MTk0NjQ0.X_NVHA._Y9Ol0gMy71RMnOkqFbBxLYPNGo');