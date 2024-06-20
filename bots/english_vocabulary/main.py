import telegram
import os
import json
import asyncio
import random


def read_questions_and_answers():
    with open("/home/buluag/gh/python_projects/bots/english_vocabulary/questions_and_answers.json", "r") as file:
        questions_and_answers = json.load(file)
        return questions_and_answers


async def format_poll(questions_and_answers):
    poll_list = []

    random_4_items = random.sample(list(questions_and_answers.items()), 4)
    poll_question, poll_answer = random.choice(random_4_items)

    for english, turkish in random_4_items:
        if english == poll_question:
            poll_list.append(turkish)
        else:
            poll_list.append(turkish)

    random.shuffle(poll_list)
    id = poll_list.index(poll_answer)

    return poll_list, poll_question, id


async def send_poll_message(poll_list, poll_question, id, CHAT_ID, bot):
    await bot.sendPoll(chat_id=CHAT_ID, question=poll_question, options=poll_list,
                       is_anonymous=True, type="quiz", allows_multiple_answers=False, correct_option_id=id)  #is_anonymous true gizli oylama demek


async def main(CHAT_ID, bot):
    ques_and_answ = read_questions_and_answers()
    poll_list, poll_question, poll_answers = await format_poll(ques_and_answ)
    await send_poll_message(poll_list, poll_question, poll_answers, CHAT_ID, bot)


if __name__ == '__main__':
    CHAT_ID = os.getenv("CHAT_ID")
    TOKEN = os.getenv("TOKEN")

    bot = telegram.Bot(TOKEN)

    if CHAT_ID is not None and TOKEN is not None:
        try:
            asyncio.run(main(CHAT_ID, bot))
        except Exception as e:
            error_log = str(e)
            print(error_log)
            error_log = error_log.split("text:", 1)[0].strip()
            raise SystemExit(error_log)
    else:
        raise SystemExit("Make sure you define chat id and token.")