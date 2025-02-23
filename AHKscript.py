from ahk import AHK
import time
from ahk import AHK
import time

ahk = AHK()

def ahk_script(num_accounts, extended_hours, start_from, stop_event, market_limit, buy_sell, delay_speed, update_status):

    def safe_send(command):
        if stop_event.is_set():
            return
        ahk.send(command)

    def safe_click():
        if stop_event.is_set():
            return
        ahk.click()

    def sleep_with_stop(duration):
        elapsed = 0
        interval = 0.1
        while elapsed < duration:
            if stop_event.is_set():
                return
            time.sleep(interval)
            elapsed += interval

    if stop_event.is_set():
        return

    if delay_speed == 'Fast':
        short_delay = 0.75
        long_delay = 1.5
        tab_delay = 0.05
    if delay_speed == 'Medium':
        short_delay = 1
        long_delay = 2
        tab_delay = 0.06
    if delay_speed == 'Slow':
        short_delay = 1.5
        long_delay = 3
        tab_delay = 0.1
    if delay_speed == 'Slower':
        short_delay = 2
        long_delay = 4
        tab_delay = 0.15

    if extended_hours == True:
        if buy_sell == 'Buy':
            first_tab = 15
            second_tab = 13
        elif buy_sell == 'Sell':
            first_tab = 17
            second_tab = 15
        if market_limit == 'Market':
            first_tab -= 2
            second_tab -= 2
    elif extended_hours == False:
        if buy_sell == 'Buy':
            first_tab = 17
            second_tab = 15
        elif buy_sell == 'Sell':
            first_tab = 19
            second_tab = 17
        if market_limit == 'Market':
            first_tab -= 2
            second_tab -= 2
    for account_num in range(start_from, num_accounts):
        account_num += 1
        if stop_event.is_set():
            break

        update_status(account_num)

        safe_click()
        sleep_with_stop(0.5)
        for _ in range(2):
            safe_send('{Tab}')
            if stop_event.is_set():
                return
        safe_send('{Enter}')

        sleep_with_stop(0.5)
        # Select the next account
        down_arrow = account_num - 2
        for _ in range(down_arrow):
            safe_send('{Down}')
            if stop_event.is_set():
                return
        sleep_with_stop(0.5)
        safe_send('{Enter}')

        sleep_with_stop(short_delay)

        for _ in range(second_tab):
            safe_send('{Tab}')
            sleep_with_stop(tab_delay)
            if stop_event.is_set():
                return
        sleep_with_stop(0.5)
        safe_send('{Enter}')
        sleep_with_stop(long_delay)
        safe_send('{Enter}')
        sleep_with_stop(short_delay)
        safe_click()

        if stop_event.is_set():
            break


def stop_script():
    global stop_event
    ahk.stop_hotkeys()
    stop_event.set()

ahk = AHK()