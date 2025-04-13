import openai
import os

# Set your API key
openai.api_key = "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"  # ← safer to use environment variable instead of hardcoding

def ask_chatgpt_for_analysis(model_output_text: str, user_query: str) -> tuple[str, str]:
    """
    Given model output and user query, calls ChatGPT API and returns an analysis and base64 image (plot).
    
    Returns:
        Tuple: (analysis_text)
    """
    prompt = f"""
    You are a helpful assistant that provides insights about Swiss startups.

    Here is the user query:
    {user_query}

    Here is the information extracted by the internal model:
    {model_output_text}

    Please write a comprehensive and complete analysis text based on the above, including also the most important numerical data.

    Please return your response formatted as clean, semantic HTML.
    Use <ul> or <ol> for lists, <strong> or <b> for bold, and <p> tags for paragraphs.

    Do not include Markdown syntax like **, just HTML.

    Wrap everything in valid HTML structure but return only the contents inside the <body> tag.

    Example output:
    <p>Here is a paragraph.</p>
    <ul><li>Item 1</li><li>Item 2</li></ul>

    """

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that returns an analysis."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        content = response.choices[0].message.content

        return content.strip()

    except Exception as e:
        print("Error communicating with OpenAI:", e)
        return "Sorry, I couldn't generate the analysis."

# Example usage
'''if __name__ == "__main__":
    info = 'in the past six months and not only increased the number of customers over 12,000, but also increased the assets managed to over 110 million CHF.Finding the donation managed to manage this growth with the existing team.The startup is still very slim with seven employees.The FinTech company develops and operates a simple, easily understandable and inexpensive investment app.The existing investors',
        'Fintech startup, founded in 2017, already has over 10,000 customers from the roof room that use the platform for digital impact investing.The platform provider currently manages over CHF 250 million, which customers have created about one of the Inyova investment products.Dillysocks sets off with fresh capital on the socks since its foundation in 2013, the startup',
       'and payment processors. In 2022, the startup became the first Swiss Fintech to be selected for the Visa Fintech Partner Connect programme, a prestigious, game-changing initiative that provides the company with access to a selection of best-in-class and trusted technology partners. To fuel this growth and string of success, the startup has secured fresh funding in a series A',
       'The Aarau FinTech startup found CHF 5 million within just 30 hours.Customers contributed the sum by crowdfunding.The startup can thus concentrate fully on the further development of the company and the app.The Fintech startup, founded by Matthias Bryner in 2019, finds and operates a simple, easily understandable and inexpensive investment app.Since market launch in February',
       'to a broad group of interested customers.At the same time, we get one step closer to our own goal of making millions of people an impact investor.Migros Bank has around one million customers.The Fintech startup, founded in 2017, already has over 10,000 customers from the roof room that use the platform for digital impact investing.The platform provider currently manages over',
       'explains: «We would like to support Migros Bank in making the topic of sustainability and the opportunities of impact investing accessible to a broad group of interested customers.At the same time, we get one step closer to our own goal of making millions of people an impact investor.Migros Bank has around one million customers.The Fintech startup, founded in 2017, already has',
       "social investment platform in the coming months and years, preparing it for a broad launch across Europe. Participants in the round include FiveT Fintech , formerly known as Avaloq Ventures and Ronald Strässle, a renowned startup investor, entrepreneuer and the startup's co-founder and Chairperson of the Board. Didier Matthey, CEO and",
       "now part of Finantix , the London based leading global provider of trusted technology to the wealth management, insurance and banking industries. The company's technologies will be integrated into the Finantix platform by augmenting it with InCube's AI, robotics, and cognitive technologies. This acquisition also allows Finatix to expand ist presence in the Swiss and global",
       'as a frontrunner in the FinTech SME lending space. The overwhelming support from Barclays and M&G reflects their confidence in our unique business model, state-of-the-art technology, and commitment to empowering the entrepreneurial SME ecosystem. We are excited about the opportunities ahead”, commented Ben James, Founder and CEO TP24. (Press',
       'Switzerland and further product development to offer a broader range of services. The investment was co-led by UBS through UBS Next , the firm’s venture and innovation unit, together with FiveT Fintech (formerly Avaloq Ventures) alongside previous investors Wingman Ventures and Seed X . In addition Numarics and UBS plan to form a strategic partnership. The',
       'braucht es starke Partnerschaften mit FinTechs wie Contovista. Unsere Kunden wollen individuelle und einfach bedienbare Lösungen. Mit dem persönlichen Finanzassistenten kommen wir diesem Bedürfnis nach und erreichen für unsere',
       'in startups from different fields ranging from healthcare, medtech and biotech to communication, hospitality, consumer products and interdisciplinary fields. During the course of the year, different financing rounds have been announced on Startupticker. In addition to the announced investment in startups like Actlight , Algrano , Bioversys , Getlocal , Inofea , Lambda Health',
       'addition, the connection of the solution to the bank is currently being implemented in implementation and interfaces to real estate management software.Evortest plans the launch for the fourth quarter of this year.For the further development phase, the Fintech startup has collected an amount of a seven-digit amount.Professional and private investors have participated."Our investors come from various, relevant industries',
       'raises a one -percent transaction fee for all deposits of the fans and the payouts to the clubs.The business model was developed in consultation with FIFA and recognized by Finma.This guarantees a solid basis and compliance with all relevant regulations, says CEO Bächtold.The Fintech startup, founded in 2023, did not collect its start-up capital at the crowd',
       'The FinTech Yapeal has completed a financing round with the aim, the strategic realignment and the growth phase promoted with full power.In addition, a CEO with many years of international experience takes over the helm.Yapeal has completed a financing round with existing and new investors.This enables Yapeal to consistently implement the strategic realignment and the focused growth strategy',
       'internationally and further develop the company’s financial engineering platform. In conjunction with the investment, Pete Casella, Senior Partner and Co-Head of Fintech investments at Point72 Ventures , joins GenTwo’s board of directors. “At Point72 Ventures we like to back founders with bold ideas. GenTwo is a good example of what we are looking',
       'million from FiveT FinTech , SICTIC and angel investors. (RAN)',
       'is a good example of what we are looking for, and we believe that the founders Patrick Loepfe and Philippe A. Naegeli are the right team to execute on their ideas,” said Pete Casella, Senior Partner and Co-Head of Fintech investments at Point72 Ventures. “We are excited to support the company on their mission towards expanding the investment',
       'is a faithfulness fintech that specializes in the automation of administration processes for SMEs in the Swiss market.The platform, founded in 2020 by Kristian Kabashi and Dominique Rey, combines AI and the expertise of certified auditors and trustees.The aim of the planned merger with Digitalbank Radicant is to offer private customers and SME companies a fully integrated offer',
       'sizeable gap between modern technologies and those that are available to banks. "This funding will enable us to further engage with the Private Banks looking to seize this opportunity, and it will facilitate the launch of our product within the Swiss market in 2025“, he adds. The company’s development team in Switzerland is already operative, working on their Wealth technology to drive the financial'
    query = "Tell me something about Fintech startups in 2010"

    analysis_text = ask_chatgpt_for_analysis(info, query)
    print("Analysis:", analysis_text)'''