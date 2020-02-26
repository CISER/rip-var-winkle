# Rip Var Winkle
...if it makes you feel better we groaned at the name when we built it.

## What does this do?

Rip Var Winkle is a microservice that accepts common statistical software files (.sav, .por, .sas7bdat, .xpt, .dta), scans for variable level metadata and sends it back as a JSON response.

Currently this JSON contains variable names and labels along with values and value labels. 

This is made possible by the lovely [pyreadstat](https://github.com/Roche/pyreadstat) library that wraps the amazing [ReadStat](https://github.com/WizardMac/ReadStat) library. Yay prior work!

## Neat... So how do I get my variables? 

Glad you asked!

Assuming the RVP server is running on `http://host:8000`, you have two options.

1. Post a multipart/form-data to `http://host:8000/` with a file upload named... `file` (super creative we know). Once uploaded and parsed you will receive JSON back containing variable metadata.

2. Post a multipart/form-data to `http://host:8000/local` with a form param named file whose value is a path to a statistical file accessible to the server. This is handy for large files as well as files you may already have.

## Can I see some example JSON?

Sure! Here is the output when the SPSS file for [this study](https://archive.ciser.cornell.edu/studies/2806) was processed by RVP.

```json
{
  "code": 200,
  "data": {
    "variable_count": 50,
    "variables": [
      {
        "label": "Unique identifier",
        "name": "uid",
        "values": []
      },
      {
        "label": "National Center for Education Statistics unique school ID",
        "name": "nces_school_id",
        "values": []
      },
      {
        "label": "Name of school",
        "name": "school_name",
        "values": []
      },
      {
        "label": "National Center for Education Statistics unique district ID",
        "name": "nces_district_id",
        "values": []
      },
      {
        "label": "Name of school district",
        "name": "district_name",
        "values": []
      },
      {
        "label": "Date of shooting",
        "name": "date",
        "values": []
      },
      {
        "label": "School year of shooting",
        "name": "school_year",
        "values": []
      },
      {
        "label": "Year of shooting",
        "name": "year",
        "values": []
      },
      {
        "label": "Approximate time of shooting",
        "name": "time",
        "values": []
      },
      {
        "label": "Day of week of shooting",
        "name": "day_of_week",
        "values": []
      },
      {
        "label": "City where school is located",
        "name": "city",
        "values": []
      },
      {
        "label": "State where school is located",
        "name": "state",
        "values": []
      },
      {
        "label": "Type of school (public or private)",
        "name": "school_type",
        "values": []
      },
      {
        "label": "Enrollment at school at time of shooting",
        "name": "enrollment",
        "values": []
      },
      {
        "label": "Number killed in shooting (excludes shooter)",
        "name": "killed",
        "values": []
      },
      {
        "label": "Number injured in shooting (excludes shooter)",
        "name": "injured",
        "values": []
      },
      {
        "label": "Number killed and injured in shooting (excludes shooter)",
        "name": "casualties",
        "values": []
      },
      {
        "label": "Type of shooting",
        "name": "shooting_type",
        "values": {
          "accidental": "Gun discharged accidentally",
          "hostage suicide": "Shooter took hostages before attempting suicide",
          "indiscriminate": "Shooter fired weapon purposefully but without intended victim(s)",
          "public suicide": "Shooter attempted suicide in public space",
          "targeted": "Shooter fired weapon purposefully with intended victim(s)",
          "unclear": "Type of shooting unknown"
        }
      },
      {
        "label": "Age of first shooter",
        "name": "age_shooter1",
        "values": []
      },
      {
        "label": "Gender of first shooter",
        "name": "gender_shooter1",
        "values": []
      },
      {
        "label": "Race or ethnicity of first shooter",
        "name": "race_ethnicity_shooter1",
        "values": {
          "a": "Asian",
          "ai": "American Indian",
          "b": "Black",
          "h": "Hispanic",
          "w": "White"
        }
      },
      {
        "label": "First shooter's relationship to school",
        "name": "shooter_relationship1",
        "values": []
      },
      {
        "label": "Flag indicating whether first shooter died in shooting",
        "name": "shooter_deceased1",
        "values": {
          "0.0": "Shooter did not die or shooter status unknown",
          "1.0": "Shooter died in shooting"
        }
      },
      {
        "label": "If first shooter deceased, how first shooter died",
        "name": "deceased_notes1",
        "values": []
      },
      {
        "label": "Age of second shooter",
        "name": "age_shooter2",
        "values": []
      },
      {
        "label": "Gender of second shooter",
        "name": "gender_shooter2",
        "values": []
      },
      {
        "label": "Race or ethnicity of second shooter",
        "name": "race_ethnicity_shooter2",
        "values": {
          "a": "Asian",
          "ai": "American Indian",
          "b": "Black",
          "h": "Hispanic",
          "w": "White"
        }
      },
      {
        "label": "Second shooter's relationship to school",
        "name": "shooter_relationship2",
        "values": []
      },
      {
        "label": "Flag indicating whether second shooter died in shooting",
        "name": "shooter_deceased2",
        "values": {
          "0.0": "Shooter did not die or shooter status unknown",
          "1.0": "Shooter died in shooting"
        }
      },
      {
        "label": "If second shooter deceased, how first shooter died",
        "name": "deceased_notes2",
        "values": []
      },
      {
        "label": "Enrollment of white students at time of shooting",
        "name": "white",
        "values": []
      },
      {
        "label": "Enrollment of black students at time of shooting",
        "name": "black",
        "values": []
      },
      {
        "label": "Enrollment of Hispanic students at time of shooting",
        "name": "hispanic",
        "values": []
      },
      {
        "label": "Enrollment of Asian students at time of shooting",
        "name": "asian",
        "values": []
      },
      {
        "label": "Enrollment of American Indian and Alaskan native students at time of shooting",
        "name": "american_indian_alaska_native",
        "values": []
      },
      {
        "label": "Enrollment of Hawaiian native and Pacific islander students at time of shooting (unavailable prior to 2009)",
        "name": "hawaiian_native_pacific_islander",
        "values": []
      },
      {
        "label": "Enrollment of students of two or more races at time of shooting (unavailable prior to 2009)",
        "name": "two_or_more",
        "values": []
      },
      {
        "label": "Flag indicating presence of school resource officer or security guard on school grounds at time of shooting",
        "name": "resource_officer",
        "values": {
          "0.0": "Resource officer of security guard not present at school at time of shooting or presence unknown",
          "1.0": "Resource officer of security guard present at school at time of shooting"
        }
      },
      {
        "label": "Weapon(s) used in shooting",
        "name": "weapon",
        "values": []
      },
      {
        "label": "Where shooter acquired weapon(s) used in shooting",
        "name": "weapon_source",
        "values": []
      },
      {
        "label": "Latitude of school",
        "name": "lat",
        "values": []
      },
      {
        "label": "Longitude of school",
        "name": "long",
        "values": []
      },
      {
        "label": "Full-time equivalent teachers at school at time of shooting",
        "name": "staffing",
        "values": []
      },
      {
        "label": "Lowest grade-level offered by school",
        "name": "low_grade",
        "values": []
      },
      {
        "label": "Highest grade-level offered at time of shooting",
        "name": "high_grade",
        "values": []
      },
      {
        "label": "Number of students at school eligible to receive a free or reduced-price lunch",
        "name": "lunch",
        "values": []
      },
      {
        "label": "County name where school is located",
        "name": "county",
        "values": []
      },
      {
        "label": "Two-digit state Federal Information Processing Standards code",
        "name": "state_fips",
        "values": []
      },
      {
        "label": "Five-digit county Federal Information Processing Standards code",
        "name": "county_fips",
        "values": []
      },
      {
        "label": "National Center for Education Statistics urban-centric locale code",
        "name": "ulocale",
        "values": {
          "11.0": "City, Large Territory inside an urbanized area and inside a principal city with population of 250,000 or more.",
          "12.0": "City, Mid-size Territory inside an urbanized area and inside a principal city with a population less than 250,000 and gr",
          "13.0": "City, Small Territory inside an urbanized area and inside a principal city with a population less than 100,000.",
          "21.0": "Suburb, Large Territory outside a principal city and inside an urbanized area with population of 250,000 or more.",
          "22.0": "Suburb, Mid-size Territory outside a principal city and inside an urbanized area with a population less than 250,000 and",
          "23.0": "Suburb, Small Territory outside a principal city and inside an urbanized area with a population less than 100,000.",
          "31.0": "Town, Fringe Territory inside an urban cluster that is less than or equal to 10 miles from an urbanized area.",
          "32.0": "Town, Distant Territory inside an urban cluster that is more than 10 miles and less than or equal to 35 miles from an ur",
          "33.0": "Town, Remote Territory inside an urban cluster that is more than 35 miles from an urbanized area.",
          "41.0": "Rural, Fringe Census-defined rural territory that is less than or equal to 5 miles from an urbanized area, as well as ru",
          "42.0": "Rural, Distant Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an urban",
          "43.0": "Rural, Remote Census-defined rural territory that is more than 25 miles from an urbanized area and is also more than 10"
        }
      }
    ]
  },
  "message": "school_shootings_data.sav parsed successfully!"
}
```

## How can I run it?

Two choices here. 

### Using gunicorn

1. Clone this repo locally.
2. Run `pip install -r requirements.txt` in the cloned directory.
3. Run `gunicorn server:app -b 0.0.0.0:8000`.
4. RVP is now listening on port 8000.

### Using Docker

1. Clone this repo locally.
2. Run `docker build . -t ripvanwinkle:latest` in the cloned directory.
3. Run `docker run --name rvp -d  -p 8000:8000 ripvarwinkle:latest`.
4. RVP is now listening on port 8000.
