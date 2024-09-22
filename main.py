import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LLMs.llm import LLM
from dotenv import load_dotenv
from graph import create_workflow

# Load environment variables from .env file
load_dotenv()


# Create the workflow
app = create_workflow(LLM)

# test instruction
# test_instruction = "Write a 5000 words, current and up to date 100% unique guide for my intermittent fasting for women over 50 cookbook on \u201cSnacks\u201d with humanlike style, using transitional phrases, and avoidance of unnatural sentence structure while explaining in details extensively and comprehensively."
test_instruction = '''Write a 5000-word in-depth analysis of the Kargil War, focusing on its historical context, key events, and the major strategic and tactical decisions made during the conflict. 

Cover the following key areas:
1. **Background:** Explain the geopolitical tensions between India and Pakistan leading up to the war, including the role of previous conflicts and the significance of the Kashmir region.

2. **Key Battles and Events:** Detail the timeline of major military operations, battles (such as the Battle of Tololing and Tiger Hill), and how the Indian Army successfully regained key positions.

3. **Strategic Importance:** Analyze the strategic significance of the Kargil district, the importance of the Line of Control (LoC), and how the terrain influenced the conduct of the war.

4. **Role of Technology and Intelligence:** Discuss the role of technological advances, such as aerial surveillance, and how intelligence failures and successes shaped the war’s progression.

5. **International Reaction:** Examine the global political implications of the war, including how major world powers like the United States reacted and their involvement in diffusing the situation.

6. **Aftermath and Legacy:** Address the war’s impact on India-Pakistan relations, defense policies, and the long-term consequences on regional stability.

7. **Themes of Patriotism and Sacrifice:** Highlight stories of individual bravery and sacrifice, and explore how the war has been remembered in Indian culture, media, and military history.'''


# Run the workflow
inputs = {"initial_prompt": test_instruction,  
          "num_steps": 0,
          "llm_name": "llama3.1-70b-groq"}
output = app.invoke(inputs)

# print(output['final_doc'])