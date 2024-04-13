class GetOccupation:
    def get_occulation(occupation):
        occupation_map = {
            "Dining/food service" : "jc_021",
            "Sales/Sales":"jc_022",
            "Travel/Leisure/Events": "jc_023",
            "Warehouse/logistics/production management":"jc_024",
            "Security":"jc_025",
            "Management/Business planning/Human resources/Administration":"jc_026",
            "Marketing/Advertisement/Promotion":"jc_027",
            "Nursery teacher/teacher/lecturer":"jc_028",
            "Driver/moving worker":"jc_012",
            "Nursing care/welfare":"jc_030"
        }
        occupation_code = occupation_map.get(occupation)
        return occupation_code