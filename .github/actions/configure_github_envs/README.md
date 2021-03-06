# Extensions for Telegram Action

Use it when you need to send telegram message

Include: 
- Gets Branch name and saves it as environment variable
- Gets Job ID and saves it environment variable

## Usage 
```yaml
- name: Add-ons for Telegram action
  uses: ./.github/actions/configure_github_envs
  if: always()
```

## Action.yml
```yaml
name: 'Addons for Telegram action'
description: 'Gets additional data for Telegram Message'
runs:
  using: "composite"
  steps:
    - name: 'Check branch name'
      run: |
        branch_name=${{ github.head_ref }}
        if ${{ github.event_name != 'pull_request' }} ; then
          branch_name=${{ github.ref }}
          branch_name=${branch_name#refs/heads/}
        fi
        echo BRANCH_NAME=$branch_name | tee -a $GITHUB_ENV
      shell: bash
    - name: 'Get Job Id Number'
      run: |
        echo Running curl
        sudo -n apt update -y ||:
        sudo -n apt install -y jq ||:
        echo 'JOB_ID<<EOF' >> $GITHUB_ENV
        curl --header "Accept: application/vnd.github.v3+json" \
        --header "Bearer: ${{ github.token }}" \
        -s https://api.github.com/repos/drakonhg/telegram-notifier/actions/runs/${{ github.run_id }}/jobs | jq -r '.jobs[0].id' | tee -a $GITHUB_ENV
        echo 'EOF' >> $GITHUB_ENV
      shell: bash
```
