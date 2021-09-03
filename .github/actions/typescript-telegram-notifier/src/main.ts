import * as core from "@actions/core";
import * as github from "@actions/github";
import axios, { AxiosResponse } from "axios";

async function run(): Promise<void> {
  try {
    core.debug("Starting...");
    const botToken: string = core.getInput("token");
    const chatId: string = core.getInput("to");
    const message: string = core.getInput("message");
    const parseMode: string = core.getInput("parse_mode");
    const disablePagePreview: boolean = core.getBooleanInput("disable_web_page_preview");
    // const gitHubToken = core.getInput("github_token");

    core.debug(
      `Sending Message, payload=${JSON.stringify(github.context.payload)}`
    );
    // await _send_message(
    //   botToken,
    //   chatId,
    //   message,
    //   parseMode,
    //   disablePagePreview
    // );
    core.debug("Message Sent");
  } catch (error: any) {
    core.setFailed(error.message);
  }
}


async function _send_message(
  botToken: string,
  chatId: string | number,
  message: string,
  parseMode: string,
  disablePagePreview: boolean
): Promise<void> {
  core.debug("Making a Request");
  const url: string = `https://api.telegram.org/bot${botToken}/sendMessage`;
  core.debug(url)
  axios.post(url, {
    chat_id: chatId,
    text: message,
    parse_mode: parseMode,
    disable_web_page_preview: disablePagePreview,
  })
      .then(res => console.log(res.data))
      .catch(err => core.debug(err))
}

run()