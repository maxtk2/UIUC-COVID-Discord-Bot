module.exports = {
    name: 'data',
    description: "This reports UIUC covid data as an embed",
    execute(message, args, Discord) {
        /*const puppeteer = require('puppeteer');
        const browser = await puppeteer.launch({
            headless: false,
        });
        const page = await browser.newPage();
        await page.setRequestInterception(true);

        await page.click('a');
        await page.waitForNavigation();

        await page.goto('https://covid19.illinois.edu/on-campus-covid-19-testing-data-dashboard/');
        await page.click('button');*/
        const currentCases = 100;
        const positivityRate = '0.5%';
        const totalTests = 1000000;
        const mostRecentDataDay = '1/1/2021';
        const newEmbed = new Discord.MessageEmbed()
        .setColor('#6897bb')
        .setTitle('Covid Data')
        .setURL('https://covid19.illinois.edu/on-campus-covid-19-testing-data-dashboard/')
        .addFields(
            {name: 'Most recent daily cases (' + mostRecentDataDay + ')', value: currentCases},
            {name: '7-day positivity rate', value: positivityRate},
            {name: 'Total tests', value: totalTests}
        )
        .setFooter('Make sure to wear your mask and practice social distancing!');

        message.channel.send(newEmbed);
    }
}