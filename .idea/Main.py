from datetime import datetime

def stampaDiTest():
    timestamp = datetime.now().strftime('%H:%M')  # Ottieni l'ora corrente e formatta come HH:MM
    return f"TestJenkins_ore{timestamp}"