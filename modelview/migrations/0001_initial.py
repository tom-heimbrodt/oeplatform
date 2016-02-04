# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 09:44
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Energymodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('acronym', models.CharField(max_length=200)),
                ('author_intitution', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('authors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('current_contact_persons', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('contact_email_address', models.EmailField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='')),
                ('short_description', models.CharField(max_length=200)),
                ('support', models.BooleanField()),
                ('documentation_user', models.BooleanField()),
                ('documentation_code', models.BooleanField()),
                ('documentation_cooperation', models.BooleanField()),
                ('documentation_quality_user', models.BooleanField()),
                ('documentation_quality_code', models.BooleanField()),
                ('documentation_quality_cooperation', models.BooleanField()),
                ('source_of_funding', models.CharField(max_length=200)),
                ('open_source', models.BooleanField()),
                ('source_downloadable', models.BooleanField()),
                ('github', models.BooleanField()),
                ('link_to_source', models.CharField(max_length=200)),
                ('open_up', models.BooleanField()),
                ('cooperative_programming', models.BooleanField()),
                ('technical_data', models.CharField(max_length=200)),
                ('modelling_software', models.CharField(max_length=200)),
                ('internal_data', models.BooleanField()),
                ('external_optimizer', models.BooleanField()),
                ('additional_software', models.CharField(max_length=200)),
                ('post_processing_facility', models.CharField(max_length=200)),
                ('modeled_energy_sectorsmobility', models.BooleanField()),
                ('modeled_energy_sectorselectricy', models.BooleanField()),
                ('modeled_energy_sectorsheat', models.BooleanField()),
                ('modelled_energy_carrier_gas', models.BooleanField()),
                ('modelled_energy_carrier_oil', models.BooleanField()),
                ('modelled_energy_carrier_electricy', models.BooleanField()),
                ('components_generation_renewable', models.BooleanField()),
                ('components_generation_conventional', models.BooleanField()),
                ('components_generation_CHP', models.BooleanField()),
                ('components_generation_dispatch', models.BooleanField()),
                ('components_transfer_heat', models.BooleanField()),
                ('components_transfer_electric', models.BooleanField()),
                ('components_transfer_gas', models.BooleanField()),
                ('user_behaviour', models.BooleanField()),
                ('user_behaviour_text', models.CharField(max_length=200)),
                ('modeled_efficiency', models.CharField(max_length=200)),
                ('market_models_text', models.CharField(max_length=200)),
                ('network_coverage_AC_load_flow', models.BooleanField()),
                ('network_coverage_DC_load_flow', models.BooleanField()),
                ('network_coverage_net_transfer_capacities', models.BooleanField()),
                ('typical_geographic_regions_covered_global', models.BooleanField()),
                ('typical_geographic_regions_covered_continental', models.BooleanField()),
                ('typical_geographic_regions_covered_national', models.BooleanField()),
                ('typical_geographic_regions_covered_regions', models.BooleanField()),
                ('typical_geographic_regions_covered_municipalities', models.BooleanField()),
                ('typical_geographic_regions_covered_districts', models.BooleanField()),
                ('typical_geographic_regions_covered_households', models.BooleanField()),
                ('typical_geographic_resolution_global', models.BooleanField()),
                ('typical_geographic_resolution_continental', models.BooleanField()),
                ('typical_geographic_resolution_national', models.BooleanField()),
                ('typical_geographic_resolution_regions', models.BooleanField()),
                ('typical_geographic_resolution_municipalities', models.BooleanField()),
                ('typical_geographic_resolution_districts', models.BooleanField()),
                ('typical_geographic_resolution_households', models.BooleanField()),
                ('typical_time_resolution_anual', models.BooleanField()),
                ('typical_time_resolution_hour', models.BooleanField()),
                ('typical_time_resolution_15_min', models.BooleanField()),
                ('typical_time_resolution_1_min', models.BooleanField()),
                ('typical_time_resolution_other', models.BooleanField()),
                ('typical_time_resolution_text', models.CharField(max_length=200)),
                ('Additional_dimensions_ecological', models.BooleanField()),
                ('Additional_dimensions_economic', models.BooleanField()),
                ('Additional_dimensions_social', models.BooleanField()),
                ('Additional_dimensions_miscellaneous', models.BooleanField()),
                ('additional_dimensions_text', models.CharField(max_length=200)),
                ('model_type_LP', models.BooleanField()),
                ('model_type_MLP', models.BooleanField()),
                ('model_type_non_linear', models.BooleanField()),
                ('model_type_Optimisation', models.BooleanField()),
                ('model_type_Simulation', models.BooleanField()),
                ('model_type_Agent_based', models.BooleanField()),
                ('model_type_Other', models.BooleanField()),
                ('model_type_text', models.CharField(max_length=200)),
                ('short_description_mathematical_model', models.CharField(max_length=200)),
                ('math_objective', models.CharField(max_length=200)),
                ('approach_to_uncertainity', models.CharField(max_length=200)),
                ('many_scenarios', models.BooleanField()),
                ('number_variables', models.IntegerField()),
                ('typical_computation_time_minutes', models.IntegerField()),
                ('typical_computation_time_hardware', models.CharField(max_length=200)),
                ('new_equations', models.CharField(max_length=200)),
                ('citation_reference', models.CharField(max_length=200)),
                ('citation_doi', models.CharField(max_length=200)),
                ('references_to_reports', models.CharField(max_length=200)),
                ('example_research_questions', models.CharField(max_length=200)),
                ('who_uses_this', models.CharField(max_length=200)),
                ('where_used', models.CharField(max_length=200)),
                ('how_validated', models.CharField(max_length=200)),
                ('model_specific_properties', models.CharField(max_length=200)),
            ],
        ),
    ]