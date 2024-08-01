import pygame
import sys
import tkinter as tk
from tkinter import filedialog
from csv_helper import create_new_csv, append_to_csv
from questions import return_questions

# Initialize Tkinter
root = tk.Tk()
root.withdraw()

# Function to get CSV file name based on user input
def get_csv_filename(participant_id, participant_name):
    return f"{participant_id}_{participant_name}_MINI_responses.csv"

# Initialize PyGame
pygame.init()

# Get monitor resolution
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BACKGROUND_COLOR = (240, 206, 115)  # Hex color #f0ce73

# Fonts
FONT = pygame.font.Font(None, 36)
LARGE_FONT = pygame.font.Font(None, 72)

# Template Questions
QUESTIONS = return_questions()

# Function to wrap text
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        current_line.append(word)
        line = ' '.join(current_line)
        if font.size(line)[0] > max_width:
            current_line.pop()
            lines.append(' '.join(current_line))
            current_line = [word]
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines

# Function to draw wrapped text in the center of the screen
def draw_wrapped_text(text, font, color, surface, y_offset=0):
    lines = wrap_text(text, font, SCREEN_WIDTH - 40)  # Margin of 20 pixels on each side
    line_height = font.get_linesize()
    total_height = line_height * len(lines)
    start_y = (SCREEN_HEIGHT - total_height) // 2 + y_offset

    for i, line in enumerate(lines):
        textobj = font.render(line, True, color)
        textrect = textobj.get_rect(center=(SCREEN_WIDTH // 2, start_y + i * line_height))
        surface.blit(textobj, textrect)

def main():
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('MINI Interface')

    # Initial variables
    current_question = 0
    responses = []
    numerical_input = ''
    participant_name = ''
    participant_id = ''
    input_active = False
    input_target = None

    # Welcome screen
    while True:
        screen.fill(BACKGROUND_COLOR)
        draw_wrapped_text("WELCOME TO MINI", LARGE_FONT, BLACK, screen)
        draw_wrapped_text("Press Enter to continue", FONT, BLACK, screen, 50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    break
        else:
            continue
        break

    # Participant information screen
    input_target = 'name'
    while True:
        screen.fill(BACKGROUND_COLOR)
        draw_wrapped_text("Participant Name:", FONT, BLACK, screen, -100)
        draw_wrapped_text(participant_name, FONT, BLACK, screen, -50)
        draw_wrapped_text("Participant ID:", FONT, BLACK, screen, 0)
        draw_wrapped_text(participant_id, FONT, BLACK, screen, 50)
        draw_wrapped_text("Press Enter to continue", FONT, BLACK, screen, 100)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if input_target == 'name' and participant_name:
                        participant_name = participant_name[:-1]
                    elif input_target == 'id' and participant_id:
                        participant_id = participant_id[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_target == 'name':
                        input_target = 'id'
                    elif input_target == 'id':
                        if participant_name and participant_id:
                            # Create a new CSV file with the name format
                            csv_file_path = get_csv_filename(participant_id, participant_name)
                            create_new_csv(csv_file_path)
                            break
                elif event.key == pygame.K_TAB:
                    input_target = 'id' if input_target == 'name' else 'name'
                else:
                    if input_target == 'name':
                        participant_name += event.unicode
                    elif input_target == 'id':
                        participant_id += event.unicode
        else:
            continue
        break

    # Main questionnaire loop
    while current_question < len(QUESTIONS):
        screen.fill(BACKGROUND_COLOR)
        question = QUESTIONS[current_question]
        draw_wrapped_text(f"{question['label']}: {question['text']}", FONT, BLACK, screen, -100)

        if question["type"] == 0:
            draw_wrapped_text("1. Yes", FONT, BLACK, screen, -50)
            draw_wrapped_text("2. No", FONT, BLACK, screen, 0)
        elif question["type"] == 1:
            draw_wrapped_text("1. Yes (Past two weeks)", FONT, BLACK, screen, -50)
            draw_wrapped_text("2. No (Past two weeks)", FONT, BLACK, screen, 0)
            draw_wrapped_text("3. Yes (Past depressive episode)", FONT, BLACK, screen, 50)
            draw_wrapped_text("4. No (Past depressive episode)", FONT, BLACK, screen, 100)
        elif question["type"] == 2:
            draw_wrapped_text("Enter your answer and press Enter:", FONT, BLACK, screen, -50)
            draw_wrapped_text(numerical_input, FONT, BLACK, screen, 0)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if question["type"] == 0:
                    if event.key == pygame.K_1:
                        responses.append((question["label"], question["text"], "Yes"))
                        current_question += 1
                    elif event.key == pygame.K_2:
                        responses.append((question["label"], question["text"], "No"))
                        current_question += 1
                elif question["type"] == 1:
                    if event.key == pygame.K_1:
                        responses.append((question["label"], question["text"], "Yes (Past two weeks)"))
                        current_question += 1
                    elif event.key == pygame.K_2:
                        responses.append((question["label"], question["text"], "No (Past two weeks)"))
                        current_question += 1
                    elif event.key == pygame.K_3:
                        responses.append((question["label"], question["text"], "Yes (Past depressive episode)"))
                        current_question += 1
                    elif event.key == pygame.K_4:
                        responses.append((question["label"], question["text"], "No (Past depressive episode)"))
                        current_question += 1
                elif question["type"] == 2:
                    if event.key == pygame.K_RETURN:
                        responses.append((question["label"], question["text"], numerical_input))
                        numerical_input = ''
                        current_question += 1
                    elif event.key == pygame.K_BACKSPACE:
                        numerical_input = numerical_input[:-1]
                    else:
                        numerical_input += event.unicode

    # Save responses to CSV
    append_to_csv(csv_file_path, [(participant_name, participant_id)] + responses)

    # Final screen
    while True:
        screen.fill(BACKGROUND_COLOR)
        draw_wrapped_text("INTERVIEW COMPLETED. THANK YOU!", LARGE_FONT, BLACK, screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
