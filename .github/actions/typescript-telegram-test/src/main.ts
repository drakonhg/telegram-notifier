import * as core from '@actions/core'
import * as github from '@actions/github'
import axios from 'axios'

async function run(): Promise<void> {
  try {
    // eslint-disable-next-line no-console
    console.log('It is starting now')
    const botToken: string = core.getInput('token')
    const chatId: string | number = core.getInput('to')
    const message: string = core.getInput('message')
    const parseMode: string = core.getInput('parse_mode')
    const disablePagePreview: boolean = core.getBooleanInput('disable_web_page_preview')
    // eslint-disable-next-line no-console

    const url: string = `https://api.telegram.org/bot${botToken}/sendMessage`

    console.log(url)

    await axios.post(url, {
      chat_id: chatId,
      text: message,
      parse_mode: parseMode,
      disable_web_page_preview: disablePagePreview
    })
        .then(res => console.log(res.status, res.data.json(), res.config))
        .catch(err => console.log(err.message))


  } catch (error: any) {
    console.log(error.message)
    core.setFailed(error.message)
  }
}

run()
