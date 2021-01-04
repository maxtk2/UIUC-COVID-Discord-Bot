module.exports = {
    name: 'deez',
    description: "This is a deez commmand, responds nuts",
    execute(message, args) {
        message.channel.send('Nuts!');
    }
}