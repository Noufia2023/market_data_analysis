

import google.generativeai as genai

genai.configure(api_key="AIzaSyB8bPp63SpgDBO4SqLGP-Z3LDOTi9kYdtc")  # pasted google API_KEY from the site

def generate_analysis_with_gemini(sector, news_list):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash") #first tried with gemini-1.5 pro, continuosly getting Gemini failed 429 error.
# sending too much information causes traffic, so in order to avoid that limit size is given
        news_text = "\n".join(news_list)
        if len(news_text) > 3000:
            news_text = news_text[:3000]

        prompt = f"""
Analyze the following market news for the {sector} sector in India. Return your answer in markdown format with:
- Title
- Sector Trends
- Recent News Highlights (3 bullets)
- Trade Opportunities (2-3 points)
- Risks (1-2 points)

News:
{news_text}
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        raise RuntimeError(f"Gemini API failed: {str(e)}")
