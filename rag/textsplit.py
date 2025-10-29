from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = '''Skip to main contenmeTeamsLocationsJob categoriesMy 
careerMy applicationsMy profileAccount securitySettingsSign outResourcesAccommodationsBenefitsInclusive 

experiencesInterview tipsLeadership principlesWorking at AmazonFAQData Engineer IJob ID: 3082667 | ADCI - BLR 14 SEZApply nowDescriptionFulfillment
 by Amazon (FBA) enables sellers to scale their businesses globally by leveraging Amazon’s world-class fulfillment network. Sellers using FBA benefit from fast, reliable shipping, Prime delivery eligibility, and hassle-free returns—allowing them to focus on growth while we handle operations. The WW FBA Central Analytics team builds and operates scalable, enterprise-grade data infrastructure, tools, and analytics solutions that power WW FBA business. We partner across global product, program, and operations teams to unify diverse datasets, deliver self-service analytics, and develop next-generation capabilities using LLMs to unlock insights.Our charter includes building the foundational pipelines, governance frameworks, and intelligent interfaces that enable internal customers to query, analyze, and act on complex datasets with natural language. This is an opportunity to work on one of the largest, complex, and critical analytics ecosystems, designing solutions that combine massive scale, high reliability, and advanced AI.We are seeking a Data Engineer I who will contribute to a GenAI-powered insights assistant initiative by developing and maintaining performant ETL pipelines and semantic layers for WW FBA metrics. Your work ensures the assistant’s text-to-SQL capabilities deliver accurate, up-to-date structured data insights supporting natural-language query responses.Key job responsibilities- Develop and maintain ETL pipelines in Spark to transform and load FBA metrics into the Data Lakehouse.- Optimize SQL queries for fast, cost-efficient access by AI systems.- Support dbt semantic models and automate metadata enrichment with Glue.- Write automated tests to ensure data quality and freshness.- Build pipelines that add business context metadata to help AI generate accurate SQL queries.Basic Qualifications- 1+ years of data engineering experience- Experience with data modeling, warehousing and building ETL pipelines- Experience with one or more query language (e.g., SQL, PL/SQL, DDL, MDX, HiveQL, SparkSQL, Scala)- Experience with one or more scripting language (e.g., Python, KornShell)Preferred Qualifications- Experience with big data technologies such as: Hadoop, Hive, Spark, EMR- Experience with any ETL tool like, Informatica, ODI, SSIS, BODI, Datastage, etc.- Proficiency in dbt, Airflow/MWAA, AWS Glue, Kinesis.- Experience building semantic layers or BI models.- Familiarity with prompt-driven SQL generation and AI-assisted query validation.Our inclusive culture empowers Amazonians to deliver the best results for our customers. If you have a disability and need a workplace accommodation or adjustment during the application and hiring process, including support for the interview or onboarding process, please visit https://amazon.jobs/content/en/how-we-hire/accommodations for more information. If the country/region you’re applying in isn’t listed, please contact your Recruiting Partner.Job detailsIND, KA, BengaluruData ScienceShare this jobJOIN US ONFind CareersJob CategoriesTeamsLocationsUS and EU Military recruitingWarehouse and Hourly JobsWorking At AmazonCultureBenefitsAmazon NewsletterInclusive experiencesOur leadership principlesHelpFAQInterview tipsReview application statusAccommodationsLegal disclosures and noticesAmazon is an equal opportunity employer and does not discriminate on the basis of protected veteran status, disability, or other legally protected status.Privacy and DataImpressum© 1996-2025'''

splitter = CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
    separator = ''
)

chunk = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
)

# res = splitter.split_text(text)

res = chunk.split_text(text)

print(res)