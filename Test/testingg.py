from bs4 import BeautifulSoup

def imitate_selector(original_selector, modified_html, target_node):
    try:
        # Parse the modified HTML using BeautifulSoup
        soup = BeautifulSoup(modified_html, 'html.parser')

        # Find the target node in the modified HTML
        found_node = soup.find(target_node.name, target_node.attrs)

        if found_node:
            # Initialize an empty selector
            proposed_selector = []

            # Extract tag name
            proposed_selector.append(found_node.name)

            # Extract attributes and their values from the target node
            target_attrs = found_node.attrs

            for attr, value in original_selector.items():
                if attr in target_attrs:
                    # If the attribute exists in the modified node, use its value
                    proposed_selector.append(f'{attr}="{target_attrs[attr]}"')
                else:
                    # If the attribute doesn't exist in the modified node, use the original value
                    proposed_selector.append(f'{attr}="{value}"')

            # Construct the proposed selector
            final_selector = ' > '.join(proposed_selector)
            return final_selector

        else:
            raise Exception("Target node not found in modified HTML.")

    except Exception as e:
        raise Exception(f"Error: {str(e)}")

# Example usage:
original_selector = {'name': 'email', 'class': 'inputtext _55r1 inputtext _1kbt inputtext _1kbt', 'id': 'email'}
modified_html = '<input type="text" class="inputtext _55r1 inputtext _1kbt inputtext _1kbt" name="gmail" id="email" >'
target_node = BeautifulSoup(modified_html, 'html.parser').find('input', {'class': 'inputtext _55r1 inputtext _1kbt inputtext _1kbt'})

proposed_selector = imitate_selector(original_selector, modified_html, target_node)
print("Proposed Selector:", proposed_selector)
