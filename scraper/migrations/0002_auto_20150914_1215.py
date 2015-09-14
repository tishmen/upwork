# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freelancer',
            name='available',
        ),
        migrations.AddField(
            model_name='scraper',
            name='category',
            field=models.CharField(null=True, choices=[('web-mobile-software-dev', 'Web, Mobile & Software Dev'), ('web-mobile-software-dev, desktop-software-development', ' - Desktop Software Development'), ('web-mobile-software-dev, ecommerce-development', ' - Ecommerce Development'), ('web-mobile-software-dev, game-development', ' - Game Development'), ('web-mobile-software-dev, mobile-development', ' - Mobile Development'), ('web-mobile-software-dev, product-management', ' - Product Management'), ('web-mobile-software-dev, qa-testing', ' - QA & Testing'), ('web-mobile-software-dev, scripts-utilities', ' - Scripts & Utilities'), ('web-mobile-software-dev, web-development', ' - Web Development'), ('web-mobile-software-dev, web-mobile-design', ' - Web & Mobile Design'), ('it-networking', 'IT & Networking'), ('it-networking, database-administration', ' - Database Administration'), ('it-networking, erp-crm-software', ' - ERP / CRM Software'), ('it-networking, information-security', ' - Information Security'), ('it-networking, network-system-administration', ' - Network & System Administration'), ('data-science-analytics', 'Data Science & Analytics'), ('data-science-analytics, a-b-testing', ' - A/B Testing'), ('data-science-analytics, data-visualization', ' - Data Visualization'), ('data-science-analytics, data-extraction-etl', ' - Data Extraction / ETL'), ('data-science-analytics, data-mining-management', ' - Data Mining & Management'), ('data-science-analytics, machine-learning', ' - Machine Learning'), ('data-science-analytics, quantitative-analysis', ' - Quantitative Analysis'), ('engineering-architecture', 'Engineering & Architecture'), ('engineering-architecture, 3d-modeling-cad', ' - 3D Modeling & CAD'), ('engineering-architecture, architecture', ' - Architecture'), ('engineering-architecture, chemical-engineering', ' - Chemical Engineering'), ('engineering-architecture, civil-structural-engineering', ' - Civil & Structural Engineering'), ('engineering-architecture, contract-manufacturing', ' - Contract Manufacturing'), ('engineering-architecture, electrical-engineering', ' - Electrical Engineering'), ('engineering-architecture, interior-design', ' - Interior Design'), ('engineering-architecture, mechanical-engineering', ' - Mechanical Engineering'), ('engineering-architecture, product-design', ' - Product Design'), ('design-creative', 'Design & Creative'), ('design-creative, animation', ' - Animation'), ('design-creative, audio-production', ' - Audio Production'), ('design-creative, graphic-design', ' - Graphic Design'), ('design-creative, illustration', ' - Illustration'), ('design-creative, logo-design-branding', ' - Logo Design & Branding'), ('design-creative, photography', ' - Photography'), ('design-creative, presentations', ' - Presentations'), ('design-creative, video-production', ' - Video Production'), ('design-creative, voice-talent', ' - Voice Talent'), ('writing', 'Writing'), ('writing, academic-writing-research', ' - Academic Writing & Research'), ('writing, article-blog-writing', ' - Article & Blog Writing'), ('writing, copywriting', ' - Copywriting'), ('writing, creative-writing', ' - Creative Writing'), ('writing, editing-proofreading', ' - Editing & Proofreading'), ('writing, grant-writing', ' - Grant Writing'), ('writing, resumes-cover-letters', ' - Resumes & Cover Letters'), ('writing, technical-writing', ' - Technical Writing'), ('writing, web-content', ' - Web Content'), ('translation', 'Translation'), ('translation, general-translation', ' - General Translation'), ('translation, legal-translation', ' - Legal Translation'), ('translation, medical-translation', ' - Medical Translation'), ('translation, technical-translation', ' - Technical Translation'), ('legal', 'Legal'), ('legal, contract-law', ' - Contract Law'), ('legal, corporate-law', ' - Corporate Law'), ('legal, criminal-law', ' - Criminal Law'), ('legal, family-law', ' - Family Law'), ('legal, intellectual-property-law', ' - Intellectual Property Law'), ('legal, paralegal-services', ' - Paralegal Services'), ('admin-support', 'Admin Support'), ('admin-support, data-entry', ' - Data Entry'), ('admin-support, personal-virtual-assistant', ' - Personal / Virtual Assistant'), ('admin-support, project-management', ' - Project Management'), ('admin-support, transcription', ' - Transcription'), ('admin-support, web-research', ' - Web Research'), ('customer-service', 'Customer Service'), ('customer-service, customer-service', ' - Customer Service'), ('customer-service, technical-support', ' - Technical Support'), ('sales-marketing', 'Sales & Marketing'), ('sales-marketing, display-advertising', ' - Display Advertising'), ('sales-marketing, email-marketing-automation', ' - Email & Marketing Automation'), ('sales-marketing, lead-generation', ' - Lead Generation'), ('sales-marketing, market-customer-research', ' - Market & Customer Research'), ('sales-marketing, marketing-strategy', ' - Marketing Strategy'), ('sales-marketing, public-relations', ' - Public Relations'), ('sales-marketing, sem-search-engine-marketing', ' - SEM - Search Engine Marketing'), ('sales-marketing, seo-search-engine-optimization', ' - SEO - Search Engine Optimization'), ('sales-marketing, smm-social-media-marketing', ' - SMM - Social Media Marketing'), ('sales-marketing, telemarketing-telesales', ' - Telemarketing & Telesales'), ('accounting-consulting', 'Accounting & Consulting'), ('accounting-consulting, accounting', ' - Accounting'), ('accounting-consulting, financial-planning', ' - Financial Planning'), ('accounting-consulting, human-resources', ' - Human Resources'), ('accounting-consulting, management-consulting', ' - Management Consulting')], max_length=250, blank=True),
        ),
        migrations.AddField(
            model_name='scraper',
            name='experience',
            field=models.CharField(null=True, choices=[('1', 'Entry'), ('2', 'Intermediate'), ('3', 'Expert')], max_length=250, blank=True),
        ),
        migrations.AddField(
            model_name='scraper',
            name='feedback',
            field=models.CharField(null=True, choices=[('45', '4.5 & up stars'), ('40', '4 & up stars'), ('30', '3 & up stars'), ('20', '2 & up stars'), ('10', '1 & up stars'), ('0', 'No feedback yet')], max_length=250, blank=True),
        ),
        migrations.AddField(
            model_name='scraper',
            name='query',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
