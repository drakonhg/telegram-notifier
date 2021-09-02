import * as core from "@actions/core";
import * as github from "@actions/github";

(async function run(): Promise<void> {
  try {
    const botToken = core.getInput("token");
    const chatId = core.getInput("to");
    const message = core.getInput("message");
    const parseMode = core.getInput("parse_mode");
    const disablePagePreview = core.getBooleanInput("disable_web_page_preview");

    const gitHubToken = core.getInput("github_token");

    core.debug(
      `Sending Message, payload=${JSON.stringify(github.context.payload)}`
    );
    await _send_message(
      botToken,
      chatId,
      message,
      parseMode,
      disablePagePreview
    );
    core.debug("Message Sent");
  } catch (error: any) {
    core.setFailed(error.message);
  }
})();

async function _send_message<T>(
  botToken: string,
  chatId: string,
  message: string,
  parseMode: string,
  disablePagePreview: boolean
): Promise<T> {
  const url = `https://api.telegram.org/bot${botToken}/sendMessage`;
  const response = await fetch(url, {
    method: "post",
    body: JSON.stringify({
      chat_id: chatId,
      text: message,
      parse_mode: parseMode,
      disable_web_page_preview: disablePagePreview,
    }),
  });

  return response.json();
}
