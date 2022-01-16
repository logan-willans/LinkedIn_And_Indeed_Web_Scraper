class JobPosting:
    # Conditional instantiation. Can instantiate with or without time_posted attribute.
    def __init__(self, job_title, company_name, info_link, description, time_posted=None):
        self.job_title = job_title
        self.company_name = company_name
        self.description = description
        self.info_link = info_link
        if time_posted is not None:
            self.time_posted = time_posted

    # Conditional toString method to account for information that might be missing
    def __str__(self):
        # What to print if all info is present
        if (hasattr(self, 'time_posted') and self.info_link is not None and self.description is not None):
            return self.job_title + "\n" + self.company_name + "\n" + self.time_posted + "\n" + self.description + "\nLink: " + self.info_link + "\n"

        # What to print if description is missing
        elif (hasattr(self, 'time_posted') and self.info_link is not None and self.description is None):
            return self.job_title + "\n" + self.company_name + "\n" + self.time_posted + "\n" + "\nLink: " + self.info_link + "\n"

        # What to print if info_link is missing
        elif (hasattr(self, 'time_posted') and self.info_link is None and self.description is not None):
            return self.job_title + "\n" + self.company_name + "\n" + self.time_posted + "\n" + self.description + "\nLink unavailable" + "\n"

        # What to print if time_posted is missing
        elif (hasattr(self, 'time_posted') == False and self.info_link is not None and self.description is not None):
            return self.job_title + "\n" + self.company_name + "\n" + self.description + "\nLink: " + self.info_link + "\n"

        # What to print if both description and info_link are missing
        elif (hasattr(self, 'time_posted') and self.info_link is None and self.description is None):
            return self.job_title + "\n" + self.company_name + "\n" + self.time_posted + "\nLink unavailable" + "\n"

        # What to print if both description and time_posted are missing
        elif (hasattr(self, 'time_posted') == False and self.info_link is not None and self.description is None):
            return self.job_title + "\n" + self.company_name + "\nLink: " + self.info_link + "\n"

        # Prints if we only have job title and company name
        else:
            return self.job_title + "\n" + self.company_name + "\n" + "Some info is missing..." + "\n"