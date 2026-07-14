def valid_phone(phone):

    return (
        phone.isdigit()
        and len(phone) == 10
    )


def valid_interview_status(status):

    return status in [
        "Scheduled",
        "Completed",
        "Cancelled",
        "Selected",
        "Rejected"
    ]


def valid_interview_mode(mode):

    return mode in [
        "Online",
        "Offline"
    ]
