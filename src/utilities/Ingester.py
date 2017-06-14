'''
    Generic data loader class that loads data from an incoming event to respective data stores
'''


class Ingester:
    def ingest(self, e, D):
        event_type = e.event_type
        event_verb = e.event_verb
        additional_data = e.additional_data

        if event_type == 'SITE_VISIT':
            D.new_sitevisit(additional_data);

        elif event_type == 'IMAGE':
            D.image_upload(additional_data);

        elif event_type == 'CUSTOMER':
            if event_verb == 'NEW':
                D.new_customer(additional_data)
            else:
                D.update_customer(additional_data)

        elif event_type == 'ORDER':
            if event_verb == 'NEW':
                D.new_order(additional_data)
            else:
                D.update_order(additional_data)