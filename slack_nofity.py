#coding: UTF-8

import slackweb

slack = slackweb.Slack(url="webhook url")
slack.notify(text="test")
