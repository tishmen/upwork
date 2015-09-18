def generate_url(category, experience, query):
    url = 'https://www.upwork.com/o/profiles/browse/'
    if category:
        url += 'c/{}/'.format(CATEGORY_MAP[category][0])
        if category[1]:
            url += 'sc/{}/'.format(CATEGORY_MAP[category][1])
    url += '?q='.format(query)
    if experience:
        url += '&ex='.format(experience)
    return url


CATEGORY_MAP = {
    # CATEGORIES
    'Web, Mobile & Software Dev': ['web-mobile-software-dev', None],
    'IT & Networking': ['it-networking', None],
    'Data Science & Analytics': ['data-science-analytics', None],
    'Engineering & Architecture': ['engineering-architecture', None],
    'Design & Creative': ['design-creative', None],
    'Writing': ['writing', None],
    'Translation': ['translation', None],
    'Legal': ['legal', None],
    'Admin Support': ['admin-support', None],
    'Customer Service': ['customer-service', None],
    'Sales & Marketing': ['sales-marketing', None],
    # SUBCATEGORIES
    'Accounting & Consulting': ['accounting-consulting', None],
    'Desktop Software Development':
        ['web-mobile-software-dev', 'desktop-software-development'],
    'Ecommerce Development':
        ['web-mobile-software-dev', 'ecommerce-development'],
    'Game Development': ['web-mobile-software-dev', 'game-development'],
    'Mobile Development': ['web-mobile-software-dev', 'mobile-development'],
    'Product Management': ['web-mobile-software-dev', 'product-management'],
    'QA & Testing': ['web-mobile-software-dev', 'qa-testing'],
    'Scripts & Utilities': ['web-mobile-software-dev', 'scripts-utilities'],
    'Web Development': ['web-mobile-software-dev', 'web-development'],
    'Web & Mobile Design': ['web-mobile-software-dev', 'web-mobile-design'],
    'Database Administration': ['it-networking', 'database-administration'],
    'ERP / CRM Software': ['it-networking', 'erp-crm-software'],
    'Information Security': ['it-networking', 'information-security'],
    'Network & System Administration':
        ['it-networking', 'network-system-administration'],
    'A/B Testing': ['data-science-analytics', 'a-b-testing'],
    'Data Visualization': ['data-science-analytics', 'data-visualization'],
    'Data Extraction / ETL': ['data-science-analytics', 'data-extraction-etl'],
    'Data Mining & Management':
        ['data-science-analytics', 'data-mining-management'],
    'Machine Learning': ['data-science-analytics', 'machine-learning'],
    'Quantitative Analysis':
        ['data-science-analytics', 'quantitative-analysis'],
    '3D Modeling & CAD': ['engineering-architecture', '3d-modeling-cad'],
    'Architecture': ['engineering-architecture', 'architecture'],
    'Chemical Engineering':
        ['engineering-architecture', 'chemical-engineering'],
    'Civil & Structural Engineering':
        ['engineering-architecture', 'civil-structural-engineering'],
    'Contract Manufacturing':
        ['engineering-architecture', 'contract-manufacturing'],
    'Electrical Engineering':
        ['engineering-architecture', 'electrical-engineering'],
    'Interior Design': ['engineering-architecture', 'interior-design'],
    'Mechanical Engineering':
        ['engineering-architecture', 'mechanical-engineering'],
    'Product Design': ['engineering-architecture', 'product-design'],
    'Animation': ['design-creative', 'animation'],
    'Audio Production': ['design-creative', 'audio-production'],
    'Graphic Design': ['design-creative', 'graphic-design'],
    'Illustration': ['design-creative', 'illustration'],
    'Logo Design & Branding': ['design-creative', 'logo-design-branding'],
    'Photography': ['design-creative', 'photography'],
    'Presentations': ['design-creative', 'presentations'],
    'Video Production': ['design-creative', 'video-production'],
    'Voice Talent': ['design-creative', 'voice-talent'],
    'Academic Writing & Research': ['writing', 'academic-writing-research'],
    'Article & Blog Writing': ['writing', 'article-blog-writing'],
    'Copywriting': ['writing', 'copywriting'],
    'Creative Writing': ['writing', 'creative-writing'],
    'Editing & Proofreading': ['writing', 'editing-proofreading'],
    'Grant Writing': ['writing', 'grant-writing'],
    'Resumes & Cover Letters': ['writing', 'resumes-cover-letters'],
    'Technical Writing': ['writing', 'technical-writing'],
    'Web Content': ['writing', 'web-content'],
    'General Translation': ['translation', 'general-translation'],
    'Legal Translation': ['translation', 'legal-translation'],
    'Medical Translation': ['translation', 'medical-translation'],
    'Technical Translation': ['translation', 'technical-translation'],
    'Contract Law': ['legal', 'contract-law'],
    'Corporate Law': ['legal', 'corporate-law'],
    'Criminal Law': ['legal', 'criminal-law'],
    'Family Law': ['legal', 'family-law'],
    'Intellectual Property Law': ['legal', 'intellectual-property-law'],
    'Paralegal Services': ['legal', 'paralegal-services'],
    'Data Entry': ['admin-support', 'data-entry'],
    'Personal / Virtual Assistant':
        ['admin-support', 'personal-virtual-assistant'],
    'Project Management': ['admin-support', 'project-management'],
    'Transcription': ['admin-support', 'transcription'],
    'Web Research': ['admin-support', 'web-research'],
    'Customer Service': ['customer-service', 'customer-service'],
    'Technical Support': ['customer-service', 'technical-support'],
    'Display Advertising': ['sales-marketing', 'display-advertising'],
    'Email & Marketing Automation':
        ['sales-marketing', 'email-marketing-automation'],
    'Lead Generation': ['sales-marketing', 'lead-generation'],
    'Market & Customer Research':
        ['sales-marketing', 'market-customer-research'],
    'Marketing Strategy': ['sales-marketing', 'marketing-strategy'],
    'Public Relations': ['sales-marketing', 'public-relations'],
    'SEM - Search Engine Marketing':
        ['sales-marketing', 'sem-search-engine-marketing'],
    'SEO - Search Engine Optimization':
        ['sales-marketing', 'seo-search-engine-optimization'],
    'SMM - Social Media Marketing':
        ['sales-marketing', 'smm-social-media-marketing'],
    'Telemarketing & Telesales':
        ['sales-marketing', 'telemarketing-telesales'],
    'Accounting': ['accounting-consulting', 'accounting'],
    'Financial Planning': ['accounting-consulting', 'financial-planning'],
    'Human Resources': ['accounting-consulting', 'human-resources'],
    'Management Consulting':
        ['accounting-consulting', 'management-consulting']
}
